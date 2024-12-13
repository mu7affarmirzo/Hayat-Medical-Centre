from datetime import datetime, timedelta
from itertools import chain
from operator import attrgetter

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from apps.decorators import role_required
from apps.logus.forms.booking import UpdateBookingForm
from apps.logus.models import BookingModel, AvailableRoomModel, AvailableRoomsTypeModel, AvailableTariffModel

BOOKINGS_PER_PAGE = 30


@role_required(role='logus', login_url='logus_auth:logout')
def get_upcoming_checkouts(request):

    search_query = request.GET.get('table_search')

    if search_query:
        bookings = sorted(get_booking_queryset(search_query), key=attrgetter('end_date'), reverse=True)
    else:
        tomorrow_date = timezone.now().date() + timedelta(days=1)
        bookings = BookingModel.objects.filter(end_date__gte=tomorrow_date)

    bookings = paginate_page(request, bookings)

    context = {
        "bookings": bookings
    }

    return render(request, 'logus/booking/checkouts.html', context)


@role_required(role='logus', login_url='logus_auth:logout')
def get_living_guests(request):
    context = {}

    check_ins = BookingModel.objects.filter(stage='settled', start_date=timezone.now().date())
    context['bookings'] = check_ins

    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')

    if search_query:
        bookings = sorted(get_booking_queryset(search_query, 'settled'), key=attrgetter('end_date'), reverse=True)
    else:
        bookings = sorted(get_booking_queryset(query, 'settled'), key=attrgetter('end_date'), reverse=True)

    bookings = paginate_page(request, bookings)

    context = {
        "bookings": bookings
    }

    return render(request, 'logus/booking/living.html', context)


@role_required(role='logus', login_url='logus_auth:logout')
def get_upcoming_check_ins_view(request):

    today = timezone.now().date()
    search_query = request.GET.get('table_search')

    if search_query:
        check_ins = sorted(get_booking_queryset(search_query), key=attrgetter('start_date'), reverse=True)
    else:
        check_ins = BookingModel.objects.filter(stage__in=['booked', 'arrived']).order_by('-start_date')

    bookings = paginate_page(request, check_ins)

    context = {
        "bookings": bookings,
        "today": today
    }

    return render(request, 'logus/booking/checkins.html', context)


@role_required(role='logus', login_url='logus_auth:logout')
def update_check_in_view(request, pk):
    today = timezone.now().date()

    booking = get_object_or_404(BookingModel, pk=pk)

    if request.method == "POST":
        form = UpdateBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('logus_booking:check-in')
        print(form.errors)
    rooms = AvailableRoomModel.objects.all()
    room_types = AvailableRoomsTypeModel.objects.all()
    tariffs = AvailableTariffModel.objects.all()

    context = {
        "booking": booking,
        "today": today,
        'rooms': rooms,
        'room_types': room_types,
        'tariffs': tariffs,
        "form": UpdateBookingForm(instance=booking),
        "stages": BookingModel.stage.field.choices
    }

    return render(request, 'logus/booking/checkins_detailed.html', context)


@login_required
def booking_search(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        bookings = BookingModel.objects.filter(name__icontains=query)
        bookings_with_series = BookingModel.objects.filter(seria__icontains=query)
        bookings = list(chain(bookings, bookings_with_series))
        results = [{
            'id': item.id, 'series': item.series, 'room': item.current_room.room_number,
            'patient': item.patient.full_name, 'tariff': item.current_tariff, 'room_type': item.current_room_type
        } for item in bookings]

        return JsonResponse(results, safe=False)
    return JsonResponse({'error': 'No query provided'}, status=400)


def paginate_page(request, queries):
    page = request.GET.get('page', 1)
    bookings_paginator = Paginator(queries, BOOKINGS_PER_PAGE)

    try:
        bookings = bookings_paginator.page(page)
    except PageNotAnInteger:
        bookings = bookings_paginator.page(BOOKINGS_PER_PAGE)
    except EmptyPage:
        bookings = bookings_paginator.page(bookings_paginator.num_pages)
    return bookings


def get_leaving_bookings_view(request):
    end_date_str = request.GET.get('end_date')
    if end_date_str:
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        return get_bookings_view(request, end_date)


def get_bookings_view(request, end_date=None):
    start_date_str = request.GET.get('start_date')
    if start_date_str:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        bookings = BookingModel.objects.filter(start_date=start_date)
    elif end_date:
        bookings = BookingModel.objects.filter(end_date=end_date)
    else:
        bookings = []

    bookings_data = [{
        'id': booking.id,
        'series': booking.series,
        'patient_full_name': booking.patient.full_name,
        'end_date': booking.end_date,
        'current_room_type': str(booking.current_room_type),
        'current_room_type_color': booking.current_room_type.color,
        'current_room_room_number': booking.current_room.room_number,
        'start_date': booking.start_date,
        'duration': booking.duration,
        'current_tariff': str(booking.current_tariff),
        'current_tariff_color': booking.current_tariff.color,
        'discount': booking.discount,
    } for booking in bookings]

    return JsonResponse({'bookings': bookings_data})


def get_booking_queryset(query=None, stage=None):
    queryset = []
    queries = query.split(" ")

    tomorrow_date = timezone.now().date() + timedelta(days=1)

    for q in queries:
        if stage:
            bookings = (BookingModel.objects.filter(stage=stage).exclude(stage='served').exclude(stage='cancelled').
                        filter(
                Q(series__icontains=q) |
                Q(patient__f_name__icontains=q) |
                Q(patient__mid_name__icontains=q)
            ).distinct())
        else:
            bookings = (BookingModel.objects.exclude(stage='served').exclude(stage='cancelled').
                        filter(start_date__gte=tomorrow_date).
                        filter(
                Q(series__icontains=q) |
                Q(patient__f_name__icontains=q) |
                Q(patient__mid_name__icontains=q)
            ).distinct())
        for new in bookings:
            queryset.append(new)

    return list(set(queryset))
