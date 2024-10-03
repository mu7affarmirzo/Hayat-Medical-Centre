from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render

from apps.account.models import PatientModel, DoctorAccountModel, NurseAccountModel, MedicalService
from apps.decorators import role_required
from apps.lis.models import LabResearchCategoryModel, LabResearchModel
from apps.logus.models import BookingModel, AvailableTariffModel, AvailableRoomModel, AvailableRoomsTypeModel
from apps.sanatorium.forms.doctors import InitialAppointmentShortForm, BasePillsInjectionsForm, \
    BaseProcedureServiceForm, BaseLabResearchServiceForm, FinalAppointmentShortForm
from apps.sanatorium.forms.patient import PatientUpdateForm, BookingModelUpdateForm, IllnessHistoryUpdateForm
from apps.sanatorium.models import IllnessHistory, DiagnosisTemplate, InitialAppointmentWithDoctorModel, \
    BasePillsInjectionsModel, BaseProcedureServiceModel, BaseLabResearchServiceModel, FinalAppointmentWithDoctorModel
from apps.warehouse.models import ItemsInStockModel

BOOKINGS_PER_PAGE = 30


@role_required(role='sanatorium.doctor', login_url='logout')
def get_title_page_by_id_view(request, pk):
    context = {
        "active_page": {'title_page': 'active'}
    }

    try:
        ill_his = IllnessHistory.objects.get(pk=pk)
    except:
        return render(request, 'sanatorium/doctors/title-page.html', context)

    if request.method == "POST":
        patient_form = PatientUpdateForm(request.POST, instance=ill_his.patient)
        ih_form = IllnessHistoryUpdateForm(request.POST, instance=ill_his)
        booking_form = BookingModelUpdateForm(request.POST, instance=ill_his.booking)

        if 'patient_form' in request.POST and patient_form.is_valid():
            patient: PatientModel = patient_form.save(commit=False)
            patient.modified_by = request.user
            patient.save()
            return redirect('sanatorium_doctors:title_page', pk=pk)
        if 'ih_form' in request.POST and ih_form.is_valid():
            ih: IllnessHistory = ih_form.save(commit=False)
            ih.modified_by = request.user
            ih.save()
            ih_form.save_m2m()
            return redirect('sanatorium_doctors:title_page', pk=pk)
        if 'booking_form' in request.POST and booking_form.is_valid():
            booking: BookingModel = booking_form.save(commit=False)
            booking.modified_by = request.user
            booking.save()
            return redirect('sanatorium_doctors:title_page', pk=pk)

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

    return render(request, 'sanatorium/doctors/title-page.html', context)


@role_required(role='sanatorium.doctor', login_url='logout')
def get_init_app_by_id_view(request, pk):
    context = {
        "active_page": {'init_app_page': 'active'},
        'doctor': request.user
    }

    try:
        ill_his = IllnessHistory.objects.get(pk=pk)
    except:
        return redirect('sanatorium_doctors:main_screen')

    init_app_instance = InitialAppointmentWithDoctorModel.objects.filter(illness_history=ill_his)

    if init_app_instance:
        init_app_form = InitialAppointmentShortForm(instance=ill_his.init_appointment)
    else:
        init_app_form = InitialAppointmentShortForm()

    if request.method == "POST":
        if init_app_instance:
            init_app_form = InitialAppointmentShortForm(request.POST, instance=ill_his.init_appointment)
        else:
            init_app_form = InitialAppointmentShortForm(request.POST)

        pills_form = BasePillsInjectionsForm(request.POST)
        procedures_form = BaseProcedureServiceForm(request.POST)
        lab_research_form = BaseLabResearchServiceForm(request.POST)

        if 'init_app_form' in request.POST and init_app_form.is_valid():
            init_app: InitialAppointmentWithDoctorModel = init_app_form.save(commit=False)
            init_app.modified_by = request.user
            init_app.created_by = request.user
            init_app.doctor = request.user
            init_app.illness_history = ill_his
            init_app.save()
            return redirect('sanatorium_doctors:init_app_page', pk=pk)
        if 'pills_form' in request.POST and pills_form.is_valid():
            pills_injections: BasePillsInjectionsModel = pills_form.save(commit=False)
            pills_injections.modified_by = request.user
            pills_injections.created_by = request.user
            pills_injections.illness_history = ill_his
            pills_injections.save()
            return redirect('sanatorium_doctors:init_app_page', pk=pk)
        if 'procedures_form' in request.POST and procedures_form.is_valid():
            procedures: BaseProcedureServiceModel = procedures_form.save(commit=False)
            procedures.modified_by = request.user
            procedures.created_by = request.user
            procedures.illness_history = ill_his
            procedures.save()
            return redirect('sanatorium_doctors:init_app_page', pk=pk)
        if 'lab_research_form' in request.POST and lab_research_form.is_valid():
            lab_research: BaseLabResearchServiceModel = lab_research_form.save(commit=False)
            lab_research.modified_by = request.user
            lab_research.created_by = request.user
            lab_research.illness_history = ill_his
            lab_research.save()
            return redirect('sanatorium_doctors:init_app_page', pk=pk)

    context['init_app_form'] = init_app_form

    context['ill_his'] = ill_his
    context['patient'] = ill_his.patient
    context['diagnosis'] = DiagnosisTemplate.objects.all()

    context['pills'] = ItemsInStockModel.objects.filter(warehouse__name='Gospital')
    context['pill_frequency_types'] = BasePillsInjectionsModel.frequency.field.choices
    context['assigned_pills'] = BasePillsInjectionsModel.objects.filter(illness_history=ill_his)

    context['assigned_procedures'] = BaseProcedureServiceModel.objects.filter(illness_history=ill_his)
    context['procedures'] = MedicalService.objects.filter(type='procedure')
    context['procedures_frequency_types'] = BaseProcedureServiceModel.frequency.field.choices

    context['labs'] = LabResearchModel.objects.all()
    context['assigned_labs'] = BaseLabResearchServiceModel.objects.filter(illness_history=ill_his)
    context['labs_types'] = LabResearchCategoryModel.objects.all()

    context['booking'] = ill_his.booking
    context['booking_history'] = ill_his.booking.booking_history.all()
    context['rooms'] = AvailableRoomModel.objects.all()
    context['room_types'] = AvailableRoomsTypeModel.objects.all()
    context['programs'] = AvailableTariffModel.objects.all()

    context['doctors'] = DoctorAccountModel.objects.all()
    context['nurses'] = NurseAccountModel.objects.all()

    return render(request, 'sanatorium/doctors/init-app-page.html', context)


@role_required(role='sanatorium.doctor', login_url='logout')
def final_appointment_view(request, pk):

    ill_his = get_object_or_404(IllnessHistory.objects.select_related('patient', 'booking'), pk=pk)

    final_app_instance = FinalAppointmentWithDoctorModel.objects.filter(illness_history=ill_his)

    if final_app_instance:
        print(ill_his.final_appointment, '------------------------------', final_app_instance)
        final_app_form = FinalAppointmentShortForm(request.POST, instance=final_app_instance.first())
    else:
        final_app_form = FinalAppointmentShortForm(request.POST)

    if request.method == "POST":
        if final_app_instance:
            final_app_form = FinalAppointmentShortForm(request.POST, instance=final_app_instance.first())
        else:
            final_app_form = FinalAppointmentShortForm(request.POST)

        if 'final_app_form' in request.POST and final_app_form.is_valid():
            final_app: FinalAppointmentWithDoctorModel = final_app_form.save(commit=False)
            final_app.modified_by = request.user
            final_app.created_by = request.user
            final_app.doctor = request.user
            final_app.illness_history = ill_his
            final_app.save()
            return redirect('sanatorium_doctors:final_appointment_page', pk=pk)
        print(final_app_form.errors)

    context = {
        "active_page": {'consulting_and_med_services_page': 'active'},

        'final_app_form': final_app_form,
        'treatment_results_choices': FinalAppointmentWithDoctorModel.treatment_results.field.choices,

        'ill_his': ill_his,
        'ill_his_types': IllnessHistory.type.field.choices,
        'diagnosis': DiagnosisTemplate.objects.all(),
        'patient': ill_his.patient,
        'booking': ill_his.booking,
        'booking_history': ill_his.booking.booking_history.all(),
        'rooms': AvailableRoomModel.objects.all(),
        'room_types': AvailableRoomsTypeModel.objects.all(),
        'programs': AvailableTariffModel.objects.all(),
        'doctors': DoctorAccountModel.objects.all(),
        'nurses': NurseAccountModel.objects.all(),
        'patient_form': PatientUpdateForm(instance=ill_his.patient),
        'ih_form': IllnessHistoryUpdateForm(instance=ill_his),
        'booking_form': BookingModelUpdateForm(instance=ill_his.booking),

        'pills': ItemsInStockModel.objects.filter(warehouse__name='Gospital'),
        'pill_frequency_types': BasePillsInjectionsModel.frequency.field.choices,
        'assigned_pills': BasePillsInjectionsModel.objects.filter(illness_history=ill_his),
        'assigned_procedures': BaseProcedureServiceModel.objects.filter(illness_history=ill_his),
        'procedures': MedicalService.objects.filter(type='procedure'),
        'procedures_frequency_types': BaseProcedureServiceModel.frequency.field.choices,
        'labs': LabResearchModel.objects.all(),
        'assigned_labs': BaseLabResearchServiceModel.objects.filter(illness_history=ill_his),
        'labs_types': LabResearchCategoryModel.objects.all(),
    }

    return render(request, 'sanatorium/doctors/final_appointment.html', context)
