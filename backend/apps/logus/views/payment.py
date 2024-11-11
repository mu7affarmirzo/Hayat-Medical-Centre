import datetime
from itertools import chain
from operator import attrgetter

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from apps.decorators import role_required
from apps.logus.forms.payment import PaymentForm
from apps.logus.models import BookingModel, Payments
from apps.sanatorium.models import IllnessHistory
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

    calculation_context = get_bookings_total_sum(target_booking, target_cheques)

    calculated_sum = calculation_context.get('total_sum', 0)
    discount_sum = int(calculated_sum*target_booking.discount/100)
    total_sum = calculated_sum - discount_sum

    if request.method == "POST":
        payment_form = PaymentForm(request.POST, instance=target_booking)

        if 'payment_form' in request.POST and payment_form.is_valid():
            payment: Payments = payment_form.save(commit=False)
            payment.booked_room = target_booking
            payment.amount = total_sum
            payment.modified_by = request.user
            payment.created_by = request.user
            payment.save()

            change_state_after_payment(target_booking, target_cheques)

            return redirect('logus_payment:debtors_list')

    context = {
        'booking': target_booking,
        'cheques': target_cheques,
        'cheques_sum': calculation_context.get('cheques_sum', 0),
        'med_services_sum': calculation_context.get('med_service_sum', 0),
        'procedures_sum': calculation_context.get('procedures_sum', 0),
        'discount_sum': discount_sum,
        'total_sum': total_sum,
        'today': datetime.date.today(),
        'transaction_type': Payments.transaction_type.field.choices
    }
    return render(request, 'logus/payment/debtor_detailed.html', context)


def change_state_after_payment(booking: BookingModel, cheques: [WarehouseChequeModel]):
    booking.stage = 'served'
    booking.save()


    for cheque in cheques:
        cheque.state = 'оплачено'
        cheque.save()

def get_bookings_total_sum(booking, target_cheques):
    context = {}
    total_sum = 0

    total_sum += booking.current_tariff.price - booking.paid_amount

    target_illness_histories = booking.illness_history.all()
    for illness_history in target_illness_histories:
        procedures_total_sum = get_assigned_procedures_sum(illness_history)
        context['procedures_sum'] = procedures_total_sum

        med_service_sum = get_assigned_med_service_sum(illness_history)
        context['med_service_sum'] = med_service_sum

        total_sum += procedures_total_sum + med_service_sum

    cheques_sum= get_cheques_sum(target_cheques)
    context['cheques_sum'] = cheques_sum

    total_sum += cheques_sum
    context['total_sum'] = total_sum

    return context


def get_cheques_sum(target_cheques):

    total_sum = 0
    for cheque in target_cheques:
        if cheque.state == 'не оплачено':
            total_sum += cheque.total_price

    return total_sum


def get_assigned_procedures_sum(illness_history: IllnessHistory):
    total_sum = 0

    current_tariff = illness_history.booking.current_tariff
    available_services = []
    if current_tariff:
        available_services = current_tariff.medical_service.all()

    procedures = illness_history.assigned_procedures.filter(state='dispatched')
    for procedure in procedures:
        service = procedure.medical_service

        if service not in available_services:
            total_sum += service.cost*procedure.done_quantity if service else 0
    return total_sum


def get_assigned_med_service_sum(illness_history: IllnessHistory):
    total_sum = 0

    current_tariff = illness_history.booking.current_tariff
    available_services = []
    if current_tariff:
        available_services = current_tariff.medical_service.all()

    procedures = illness_history.assigned_med_services.filter(state='dispatched')
    for procedure in procedures:
        service = procedure.medical_service

        if service not in available_services:
            total_sum += service.cost if service else 0
    return total_sum


@role_required(role='logus', login_url='logus_auth:logout')
def proceed_payment(request, pk):
    target_booking = get_object_or_404(BookingModel, pk=pk)

    return render(request, 'logus/payment/proceed_payment.html', {})


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
