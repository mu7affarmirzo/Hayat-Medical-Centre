from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta
from itertools import chain
from operator import attrgetter

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from apps.decorators import role_required
from apps.logus.models import BookingModel

BOOKINGS_PER_PAGE = 30


def main_screen_view(request):
    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')

    if search_query:
        bookings = sorted(get_booking_queryset(search_query, 'settled'), key=attrgetter('end_date'), reverse=True)
    else:
        bookings = sorted(get_booking_queryset(query, 'settled'), key=attrgetter('end_date'), reverse=True)

    page = request.GET.get('page', 1)
    bookings_paginator = Paginator(bookings, BOOKINGS_PER_PAGE)

    try:
        bookings = bookings_paginator.page(page)
    except PageNotAnInteger:
        bookings = bookings_paginator.page(BOOKINGS_PER_PAGE)
    except EmptyPage:
        bookings = bookings_paginator.page(bookings_paginator.num_pages)

    context = {
        "bookings": bookings
    }

    return render(request, 'sanatorium/staff/main_screen.html', context)


def get_patients_list(request):
    context = {}

    return render(request, 'sanatorium/staff/main_screen.html', context)


def get_bookings_by_start_date_view(request):
    start_date_str = request.GET.get('start_date')
    if start_date_str:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        return get_bookings_view(request, start_date)


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
