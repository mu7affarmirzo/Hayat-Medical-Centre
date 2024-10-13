from audioop import error

from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render

from apps.account.models import PatientModel, DoctorAccountModel, NurseAccountModel, MedicalService
from apps.decorators import role_required
from apps.lis.models import LabResearchCategoryModel, LabResearchModel
from apps.logus.models import BookingModel, AvailableTariffModel, AvailableRoomModel, AvailableRoomsTypeModel
from apps.sanatorium.forms.doctors import InitialAppointmentShortForm, BasePillsInjectionsForm, \
    BaseProcedureServiceForm, BaseLabResearchServiceForm, FinalAppointmentShortForm, \
    ConsultingWithCardiologistShortForm, ConsultingWithNeurologistShortForm, \
    AppointmentWithOnDutyDoctorOnArrivalShortForm, RepeatedAppointmentWithDoctorShortForm
from apps.sanatorium.forms.patient import PatientUpdateForm, BookingModelUpdateForm, IllnessHistoryUpdateForm
from apps.sanatorium.models import IllnessHistory, DiagnosisTemplate, InitialAppointmentWithDoctorModel, \
    BasePillsInjectionsModel, BaseProcedureServiceModel, BaseLabResearchServiceModel, FinalAppointmentWithDoctorModel, \
    ConsultingWithCardiologistModel, ConsultingWithNeurologistModel, AppointmentWithOnDutyDoctorOnArrivalModel, \
    RepeatedAppointmentWithDoctorModel, AppointmentWithOnDutyDoctorModel, EkgAppointmentModel
from apps.warehouse.models import ItemsInStockModel

BOOKINGS_PER_PAGE = 30


def get_all_appointments(ill_his):
    return {
        'cardiologist_appointments': ConsultingWithCardiologistModel.objects.filter(illness_history=ill_his),
        'neurologist_appointments': ConsultingWithNeurologistModel.objects.filter(illness_history=ill_his),
        'on_arrival_appointments': AppointmentWithOnDutyDoctorOnArrivalModel.objects.filter(illness_history=ill_his),
        'repeated_appointments': RepeatedAppointmentWithDoctorModel.objects.filter(illness_history=ill_his),
        'with_doc_on_duty_appointments': AppointmentWithOnDutyDoctorModel.objects.filter(illness_history=ill_his),
        'ekg_appointments': EkgAppointmentModel.objects.filter(illness_history=ill_his),
        'final_appointment': FinalAppointmentWithDoctorModel.objects.filter(illness_history=ill_his).first()
    }


def assemble_context(ill_his, active_page='consulting_and_med_services_page'):
    context = {
        "active_page": {active_page: 'active'},

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
        **get_all_appointments(ill_his),
    }

    return context

@role_required(role='sanatorium.doctor', login_url='logout')
def get_title_page_by_id_view(request, pk):

    try:
        ill_his = IllnessHistory.objects.get(pk=pk)
    except:
        return render(request, 'sanatorium/doctors/title-page.html', {"active_page": {'title_page': 'active'}})

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

    context = assemble_context(ill_his, 'title_page')

    return render(request, 'sanatorium/doctors/title-page.html', context)


@role_required(role='sanatorium.doctor', login_url='logout')
def get_init_app_by_id_view(request, pk):

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
    context = assemble_context(ill_his)
    context.update({
        'doctor': request.user,
        'init_app_form': init_app_form,
    })

    return render(request, 'sanatorium/doctors/appointments/init-app-page.html', context)


@role_required(role='sanatorium.doctor', login_url='logout')
def final_appointment_view(request, pk):

    ill_his = get_object_or_404(IllnessHistory.objects.select_related('patient', 'booking'), pk=pk)

    final_app_instance = FinalAppointmentWithDoctorModel.objects.filter(illness_history=ill_his)

    if final_app_instance:
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

    context = assemble_context(ill_his)
    context.update({
        'final_app_form': final_app_form,
        'treatment_results_choices': FinalAppointmentWithDoctorModel.treatment_results.field.choices,
    })

    return render(request, 'sanatorium/doctors/appointments/final_appointment.html', context)


@role_required(role='sanatorium.doctor', login_url='logout')
def cardiologist_appointment_view(request, pk):

    ill_his = get_object_or_404(IllnessHistory.objects.select_related('patient', 'booking'), pk=pk)

    cardiologist_app_instance = ConsultingWithCardiologistModel.objects.filter(illness_history=ill_his).first()

    context = assemble_context(ill_his)

    if request.method == "POST":
        cardiologist_app_form = ConsultingWithCardiologistShortForm(request.POST or None, request.FILES or None, instance=cardiologist_app_instance)
        if cardiologist_app_form.is_valid():
            cardiologist_app: ConsultingWithCardiologistModel = cardiologist_app_form.save(commit=False)
            cardiologist_app.modified_by = request.user
            cardiologist_app.created_by = request.user
            cardiologist_app.doctor = request.user
            cardiologist_app.illness_history = ill_his
            cardiologist_app.save()
            return redirect('sanatorium_doctors:main_screen')
        else:
            context['cardiologist_app_form'] = cardiologist_app_form
            return render(request, 'sanatorium/doctors/appointments/cardiologist_appointment.html', context)
    else:
        cardiologist_app_form = ConsultingWithCardiologistShortForm(instance=cardiologist_app_instance)

    context['cardiologist_app_form'] = cardiologist_app_form
    context['state_choices'] = ConsultingWithCardiologistModel.state.field.choices

    return render(request, 'sanatorium/doctors/appointments/cardiologist_appointment.html', context)


@role_required(role='sanatorium.doctor', login_url='logout')
def neurologist_appointment_view(request, pk):

    ill_his = get_object_or_404(IllnessHistory.objects.select_related('patient', 'booking'), pk=pk)

    neurologist_app_instance = ConsultingWithNeurologistModel.objects.filter(illness_history=ill_his).first()

    context = assemble_context(ill_his)

    if request.method == "POST":
        neurologist_app_form = ConsultingWithNeurologistShortForm(request.POST or None, request.FILES or None, instance=neurologist_app_instance)
        if neurologist_app_form.is_valid():
            neurologist_app: ConsultingWithNeurologistModel = neurologist_app_form.save(commit=False)
            neurologist_app.modified_by = request.user
            neurologist_app.created_by = request.user
            neurologist_app.doctor = request.user
            neurologist_app.illness_history = ill_his
            neurologist_app.save()
            return redirect('sanatorium_doctors:main_screen')
        else:
            print(neurologist_app_form.errors)
            context['neurologist_app_form'] = neurologist_app_form
            return render(request, 'sanatorium/doctors/appointments/neurologist_appointment.html', context)
    else:
        neurologist_app_form = ConsultingWithNeurologistShortForm(instance=neurologist_app_instance)

    context['neurologist_app_form'] = neurologist_app_form
    context['state_choices'] = ConsultingWithNeurologistModel.state.field.choices

    return render(request, 'sanatorium/doctors/appointments/neurologist_appointment.html', context)


@role_required(role='sanatorium.doctor', login_url='logout')
def on_arrival_appointments_view(request, pk):

    ill_his = get_object_or_404(IllnessHistory.objects.select_related('patient', 'booking'), pk=pk)

    on_arrival_app_instance = AppointmentWithOnDutyDoctorOnArrivalModel.objects.filter(illness_history=ill_his).first()

    context = assemble_context(ill_his)

    if request.method == "POST":
        on_arrival_app_form = AppointmentWithOnDutyDoctorOnArrivalShortForm(request.POST or None, request.FILES or None, instance=on_arrival_app_instance)
        if on_arrival_app_form.is_valid():
            on_arrival_app: AppointmentWithOnDutyDoctorOnArrivalModel = on_arrival_app_form.save(commit=False)
            on_arrival_app.modified_by = request.user
            on_arrival_app.created_by = request.user
            on_arrival_app.doctor = request.user
            on_arrival_app.illness_history = ill_his
            on_arrival_app.save()
            return redirect('sanatorium_doctors:main_screen')
        else:
            print(on_arrival_app_form.errors)
            context['on_arrival_app_form'] = on_arrival_app_form
            return render(request, 'sanatorium/doctors/appointments/on_arrival_appointment.html', context)
    else:
        on_arrival_app_form = AppointmentWithOnDutyDoctorOnArrivalShortForm(instance=on_arrival_app_instance)

    context['on_arrival_app_form'] = on_arrival_app_form
    context['state_choices'] = AppointmentWithOnDutyDoctorOnArrivalModel.state.field.choices

    return render(request, 'sanatorium/doctors/appointments/on_arrival_appointment.html', context)


@role_required(role='sanatorium.doctor', login_url='logout')
def repeated_appointments_view(request, pk):

    ill_his = get_object_or_404(IllnessHistory.objects.select_related('patient', 'booking'), pk=pk)

    repeated_app_instance = RepeatedAppointmentWithDoctorModel.objects.filter(illness_history=ill_his).first()

    context = assemble_context(ill_his)

    if request.method == "POST":
        repeated_app_form = RepeatedAppointmentWithDoctorShortForm(request.POST or None, request.FILES or None, instance=repeated_app_instance)
        if repeated_app_form.is_valid():
            repeated_app: RepeatedAppointmentWithDoctorModel = repeated_app_form.save(commit=False)
            repeated_app.modified_by = request.user
            repeated_app.created_by = request.user
            repeated_app.doctor = request.user
            repeated_app.illness_history = ill_his
            repeated_app.save()
            return redirect('sanatorium_doctors:main_screen')
        else:
            context['repeated_app_form'] = repeated_app_form
            return render(request, 'sanatorium/doctors/appointments/repeated_appointment.html', context)
    else:
        repeated_app_form = RepeatedAppointmentWithDoctorShortForm(instance=repeated_app_instance)

    context['repeated_app_form'] = repeated_app_form
    context['state_choices'] = RepeatedAppointmentWithDoctorModel.state.field.choices

    return render(request, 'sanatorium/doctors/appointments/repeated_appointment.html', context)


@role_required(role='sanatorium.doctor', login_url='logout')
def update_repeated_appointments_view(request, pk):

    repeated_app_instance = get_object_or_404(RepeatedAppointmentWithDoctorModel, pk=pk)

    ill_his = repeated_app_instance.illness_history

    context = assemble_context(ill_his)

    if request.method == "POST":
        if request.user != repeated_app_instance.created_by:
            return redirect('sanatorium_doctors:main_screen')

        repeated_app_form = RepeatedAppointmentWithDoctorShortForm(request.POST or None, request.FILES or None, instance=repeated_app_instance)
        if repeated_app_form.is_valid():
            repeated_app: RepeatedAppointmentWithDoctorModel = repeated_app_form.save(commit=False)
            repeated_app.modified_by = request.user
            repeated_app.save()
            return redirect('sanatorium_doctors:main_screen')
        else:
            context['repeated_app_form'] = repeated_app_form
            return render(request, 'sanatorium/doctors/appointments/repeated_appointment.html', context)
    else:
        repeated_app_form = RepeatedAppointmentWithDoctorShortForm(instance=repeated_app_instance)
        context['repeated_app_form'] = repeated_app_form
        context['state_choices'] = RepeatedAppointmentWithDoctorModel.state.field.choices

        return render(request, 'sanatorium/doctors/appointments/repeated_appointment.html', context)