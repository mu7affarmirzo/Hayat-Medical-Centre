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
from apps.sanatorium.forms.doctors import InitialAppointmentShortForm, BasePillsInjectionsForm, \
    BaseProcedureServiceForm, BaseLabResearchServiceForm
from apps.sanatorium.forms.patient import PatientUpdateForm, BookingModelUpdateForm, IllnessHistoryUpdateForm
from apps.sanatorium.models import IllnessHistory, DiagnosisTemplate, InitialAppointmentWithDoctorModel, \
    BasePillsInjectionsModel, BaseProcedureServiceModel, BaseLabResearchServiceModel
from apps.warehouse.models import ItemsInStockModel

BOOKINGS_PER_PAGE = 30


@role_required(role='sanatorium.doctor', login_url='logout')
def main_screen_view(request):
    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')

    if search_query:
        bookings = sorted(get_booking_queryset(search_query, 'settled'), key=attrgetter('booking.end_date'), reverse=True)
    else:
        bookings = sorted(get_booking_queryset(query, 'settled'), key=attrgetter('booking.end_date'), reverse=True)

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

    return render(request, 'sanatorium/doctors/main_screen.html', context)


@role_required(role='sanatorium.doctor', login_url='logout')
def get_patients_list(request):
    context = {}

    return render(request, 'sanatorium/doctors/main_screen.html', context)


@role_required(role='sanatorium.doctor', login_url='logout')
def get_patient_by_id_view(request, pk):
    context = {}

    try:
        ill_his = IllnessHistory.objects.get(pk=pk)
    except:
        return render(request, 'sanatorium/doctors/patient.html', context)

    if request.method == "POST":
        patient_form = PatientUpdateForm(request.POST, instance=ill_his.patient)
        ih_form = IllnessHistoryUpdateForm(request.POST, instance=ill_his)
        booking_form = BookingModelUpdateForm(request.POST, instance=ill_his.booking)

        if 'patient_form' in request.POST and patient_form.is_valid():
            patient: PatientModel = patient_form.save(commit=False)
            patient.modified_by = request.user
            patient.save()
            return redirect('sanatorium_staff:get_patient_by_id', pk=pk)
        if 'ih_form' in request.POST and ih_form.is_valid():
            ih: IllnessHistory = ih_form.save(commit=False)
            ih.modified_by = request.user
            ih.save()
            ih_form.save_m2m()
            return redirect('sanatorium_staff:get_patient_by_id', pk=pk)
        if 'booking_form' in request.POST and booking_form.is_valid():
            booking: BookingModel = booking_form.save(commit=False)
            booking.modified_by = request.user
            booking.save()
            return redirect('sanatorium_staff:get_patient_by_id', pk=pk)

    context['ill_his'] = ill_his
    context['ill_his_types'] = IllnessHistory.type.field.choices
    context['patient'] = ill_his.patient

    context['booking'] = ill_his.booking
    context['booking_history'] = ill_his.booking.booking_history.all()
    context['rooms'] = AvailableRoomModel.objects.all()
    context['room_types'] = AvailableRoomsTypeModel.objects.all()
    context['programs'] = AvailableTariffModel.objects.all()

    context['doctors'] = DoctorAccountModel.objects.all()
    context['nurses'] = NurseAccountModel.objects.all()

    patient_form = PatientUpdateForm(instance=ill_his.patient)
    ih_form = IllnessHistoryUpdateForm(instance=ill_his)
    booking_form = BookingModelUpdateForm(instance=ill_his.booking)

    context["patient_form"] = patient_form
    context["ih_form"] = ih_form
    context["booking_form"] = booking_form

    return render(request, 'sanatorium/doctors/patient.html', context)


@role_required(role='sanatorium.doctor', login_url='logout')
def get_bookings_by_start_date_view(request):
    start_date_str = request.GET.get('start_date')
    if start_date_str:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        return get_bookings_view(request, start_date)


def get_booking_queryset(query=None, stage=None):
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


def get_labs_view(request, category_id):
    print('hellooo\n\n\n\n\n')
    speciality = get_object_or_404(LabResearchCategoryModel, id=category_id)
    labs = LabResearchModel.objects.filter(category=speciality).values('id', 'name')
    return JsonResponse(list(labs), safe=False)
