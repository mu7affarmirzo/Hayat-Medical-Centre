from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from itertools import chain
from operator import attrgetter

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from apps.account.models import PatientModel, DoctorAccountModel, NurseAccountModel, MedicalService, SpecialityModel
from apps.decorators import role_required
from apps.lis.models import LabResearchCategoryModel, LabResearchModel
from apps.logus.models import BookingModel, AvailableTariffModel, AvailableRoomModel, AvailableRoomsTypeModel
from apps.logus.views.bookings import get_bookings_view
from apps.sanatorium.forms.dispatchers import DispatchBaseProcedureServiceForm, ProcedureDaysModelForm
from apps.sanatorium.forms.doctors import InitialAppointmentShortForm, BasePillsInjectionsForm, \
    BaseProcedureServiceForm, BaseLabResearchServiceForm
from apps.sanatorium.forms.patient import PatientUpdateForm, BookingModelUpdateForm, IllnessHistoryUpdateForm
from apps.sanatorium.models import IllnessHistory, DiagnosisTemplate, InitialAppointmentWithDoctorModel, \
    BasePillsInjectionsModel, BaseProcedureServiceModel, BaseLabResearchServiceModel, ProcedureDaysModel
from apps.warehouse.models import ItemsInStockModel

BOOKINGS_PER_PAGE = 30


@role_required(role='sanatorium.dispatcher', login_url='logout')
def get_patients_list(request):
    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')

    doctor = DoctorAccountModel.objects.filter(doctor=request.user).first()
    if not doctor:
        return render(request, 'sanatorium/dispatcher/main_screen.html', {})

    if search_query:
        bookings = sorted(get_booking_queryset(search_query, 'settled', doctor), key=attrgetter('booking.end_date'),
                          reverse=True)
    else:
        bookings = sorted(get_booking_queryset(query, 'settled', doctor), key=attrgetter('booking.end_date'), reverse=True)

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

    return render(request, 'sanatorium/dispatcher/main_screen.html', context)


@role_required(role='sanatorium.dispatcher', login_url='logout')
def get_patient_procedures_view(request, pk):
    context = {}

    try:
        ill_his = IllnessHistory.objects.get(pk=pk)
    except:
        return render(request, 'sanatorium/dispatcher/main_screen.html', context)

    context['ill_his'] = ill_his
    context['assigned_procedures'] = BaseProcedureServiceModel.objects.filter(illness_history=ill_his).order_by('-created_at')
    context['booking'] = ill_his.booking
    context['booking_history'] = ill_his.booking.booking_history.all()

    return render(request, 'sanatorium/dispatcher/patient_procedures.html', context)


@role_required(role='sanatorium.dispatcher', login_url='logout')
def dispatch_patient_procedures_view(request, pk):
    context = {}

    try:
        procedure = BaseProcedureServiceModel.objects.get(pk=pk)
    except:
        return render(request, 'sanatorium/dispatcher/main_screen.html', context)

    ill_his = procedure.illness_history

    if request.method == "POST":
        form = DispatchBaseProcedureServiceForm(request.POST, instance=procedure)
        if form.is_valid():
            procedure = form.save(commit=False)
            procedure.updated_by = request.user
            procedure.state = 'dispatched'
            procedure.save()

            days = ProcedureDaysModel.objects.filter(procedure=procedure)
            for day in days:
                day.procedure_doctor = procedure.procedure_doctor
                day.state = 'диспетчеризирован'
                day.save()

            return redirect('sanatorium_dispatchers:patient_procedure_by_days', pk=pk)

    form = DispatchBaseProcedureServiceForm(instance=procedure)
    context['ill_his'] = procedure.illness_history
    context['procedure'] = procedure
    context['days'] = procedure.days.all()
    context['booking'] = ill_his.booking
    context['booking_history'] = ill_his.booking.booking_history.all()
    context['specialists'] = DoctorAccountModel.objects.filter(specialty_type__name='treatment')
    context['dispatch_form'] = form

    return render(request, 'sanatorium/dispatcher/patient_procedure_dispatch.html', context)


@role_required(role='sanatorium.dispatcher', login_url='logout')
def update_procedure_days_view(request, pk):
    context = {}

    try:
        days = ProcedureDaysModel.objects.get(pk=pk)
    except:
        return redirect('sanatorium_dispatchers:main_screen')

    procedure = days.procedure
    ill_his = procedure.illness_history

    if request.method == "POST":
        form = ProcedureDaysModelForm(request.POST, instance=days)
        target_time = datetime.strptime(form.data.get('start_at'), '%m/%d/%Y %I:%M %p')
        days.updated_by = request.user
        days.state = form.data.get('state')
        days.start_at = target_time
        days.procedure_doctor_id = form.data.get('procedure_doctor')
        days.comments = form.data.get('comments')
        days.save()
        return redirect('sanatorium_dispatchers:patient_procedure_by_days', pk=procedure.pk)

    form = ProcedureDaysModelForm(instance=days)
    context['specialists'] = DoctorAccountModel.objects.filter(specialty_type__name='treatment')
    context['form'] = form
    context['states'] = ProcedureDaysModel.state.field.choices
    context['ill_his'] = ill_his

    return render(request, 'sanatorium/dispatcher/update_days.html', context)


@role_required(role='sanatorium.dispatcher', login_url='logout')
def get_patient_procedure_by_days_view(request, pk):
    context = {}

    try:
        procedure = BaseProcedureServiceModel.objects.get(pk=pk)
    except:
        return render(request, 'sanatorium/dispatcher/main_screen.html', context)

    ill_his = procedure.illness_history

    context['ill_his'] = procedure.illness_history
    context['procedure'] = procedure
    context['days'] = procedure.days.all()
    context['booking'] = ill_his.booking
    context['booking_history'] = ill_his.booking.booking_history.all()
    context['specialists'] = DoctorAccountModel.objects.filter(specialty_type__name='treatment')

    return render(request, 'sanatorium/dispatcher/patient_procedure_by_days.html', context)


@role_required(role='sanatorium.dispatcher', login_url='logout')
def get_bookings_by_start_date_view(request):
    start_date_str = request.GET.get('start_date')
    if start_date_str:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        return get_bookings_view(request, start_date)


def get_booking_queryset(query=None, stage=None, doctor=None):
    queryset = []
    queries = query.split(" ")

    tomorrow_date = timezone.now().date() + timedelta(days=1)

    for q in queries:
        if stage:
            bookings = (IllnessHistory.objects.filter(booking__stage=stage).exclude(booking__stage='served').exclude(booking__stage='cancelled').
                        filter(
                Q(series_number__icontains=q) |
                Q(patient__f_name__icontains=q) |
                Q(patient__mid_name__icontains=q)
            ).distinct())
        else:
            bookings = (IllnessHistory.objects.exclude(booking__stage='served').exclude(booking__stage='cancelled').
                        filter(booking__start_date__gte=tomorrow_date).
                        filter(
                Q(series_number__icontains=q) |
                Q(patient__f_name__icontains=q) |
                Q(patient__mid_name__icontains=q)
            ).distinct())
        for new in bookings:
            queryset.append(new)

    return list(set(queryset))

