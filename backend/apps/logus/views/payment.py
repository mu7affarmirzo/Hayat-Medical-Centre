from datetime import datetime, timedelta
from itertools import chain
from operator import attrgetter

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from apps.decorators import role_required
from apps.logus.models import BookingModel
from apps.warehouse.models import WarehouseChequeModel

BOOKINGS_PER_PAGE = 30


@role_required(role='logus', login_url='logus_auth:logout')
def get_debtors_list(request):

    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')

    if search_query:
        bookings = sorted(get_debtors_queryset(search_query), key=attrgetter('end_date'), reverse=True)
    else:
        bookings = sorted(get_debtors_queryset(query), key=attrgetter('end_date'), reverse=True)

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

    return render(request, 'logus/payment/debtors.html', context)


@role_required(role='logus', login_url='logus_auth:logout')
def get_debtor_detailed(request, pk):
    target_booking = get_object_or_404(BookingModel, pk=pk)
    target_cheques = WarehouseChequeModel.objects.filter(illness_history__in=target_booking.illness_history.all())

    context = {
        'booking': target_booking,
        'cheques': target_cheques
    }
    return render(request, 'logus/payment/debtor_detailed.html', context)


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


def get_debtors_queryset(query=None):
    queryset = []
    queries = query.split(" ")

    for q in queries:
        bookings = (BookingModel.objects.exclude(stage='served').exclude(stage='cancelled').
                    filter(
            Q(series__icontains=q) |
            Q(patient__f_name__icontains=q) |
            Q(patient__mid_name__icontains=q)
        ).distinct())
        for new in bookings:
            queryset.append(new)

    return list(set(queryset))
