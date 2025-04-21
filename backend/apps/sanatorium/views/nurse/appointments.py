from audioop import error

from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render

from apps.account.models import PatientModel, DoctorAccountModel, NurseAccountModel, MedicalService
from apps.decorators import role_required
from apps.lis.models import LabResearchCategoryModel, LabResearchModel
from apps.logus.models import BookingModel, AvailableTariffModel, AvailableRoomModel, AvailableRoomsTypeModel
from apps.sanatorium.forms.doctors import InitialAppointmentShortForm, BasePillsInjectionsForm, \
    BaseProcedureServiceForm, BaseLabResearchServiceForm, FinalAppointmentShortForm, \
    ConsultingWithCardiologistShortForm, ConsultingWithNeurologistShortForm, \
    AppointmentWithOnDutyDoctorOnArrivalShortForm, RepeatedAppointmentWithDoctorShortForm, \
    AppointmentWithOnDutyDoctorForm, EkgAppointmentShortForm, InitialAppointmentWithDoctorForm
from apps.sanatorium.forms.patient import PatientUpdateForm, BookingModelUpdateForm, IllnessHistoryUpdateForm
from apps.sanatorium.models import IllnessHistory, DiagnosisTemplate, InitialAppointmentWithDoctorModel, \
    BasePillsInjectionsModel, BaseProcedureServiceModel, BaseLabResearchServiceModel, FinalAppointmentWithDoctorModel, \
    ConsultingWithCardiologistModel, ConsultingWithNeurologistModel, AppointmentWithOnDutyDoctorOnArrivalModel, \
    RepeatedAppointmentWithDoctorModel, AppointmentWithOnDutyDoctorModel, EkgAppointmentModel
from apps.warehouse.models import ItemsInStockModel, ChequeItemsModel

BOOKINGS_PER_PAGE = 30


def is_author(current_user, author):
    return current_user == author

def show_error_message(request, message):
    messages.error(request, message)

def redirect_to_main_screen():
    return redirect('sanatorium_doctors:main_screen')

def save_modified_appointment(appointment_form, user):
    appointment_instance = appointment_form.save(commit=False)
    appointment_instance.modified_by = user
    appointment_instance.save()


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
        'pill_frequency_types': ChequeItemsModel.frequency.field.choices,
        'assigned_pills': ChequeItemsModel.objects.filter(cheque__illness_history=ill_his),
        'assigned_procedures': BaseProcedureServiceModel.objects.filter(illness_history=ill_his),
        'procedures': MedicalService.objects.filter(type='procedure'),
        'procedures_frequency_types': BaseProcedureServiceModel.frequency.field.choices,
        'labs': LabResearchModel.objects.all(),
        'assigned_labs': BaseLabResearchServiceModel.objects.filter(illness_history=ill_his),
        'labs_types': LabResearchCategoryModel.objects.all(),
        **get_all_appointments(ill_his),
    }

    return context

@role_required(role='sanatorium.nurse', login_url='logout')
def get_title_page_by_id_view(request, pk):

    try:
        ill_his = IllnessHistory.objects.get(pk=pk)
    except:
        return render(request, 'sanatorium/nurse/title-page.html', {"active_page": {'title_page': 'active'}})

    context = assemble_context(ill_his, 'title_page')

    return render(request, 'sanatorium/nurse/title-page.html', context)


@role_required(role='sanatorium.nurse', login_url='logout')
def get_init_app_by_id_view(request, pk):

    try:
        ill_his = IllnessHistory.objects.get(pk=pk)
    except:
        return redirect('sanatorium_doctors:main_screen')

    init_app_instance = InitialAppointmentWithDoctorModel.objects.filter(illness_history=ill_his)

    if init_app_instance:
        init_app_form = InitialAppointmentWithDoctorForm(instance=ill_his.init_appointment)
    else:
        init_app_form = InitialAppointmentWithDoctorForm()

    context = assemble_context(ill_his)
    context.update({
        'doctor': request.user,
        'init_app_form': init_app_form,
    })

    return render(request, 'sanatorium/nurse/appointments/init-app-page.html', context)


@role_required(role='sanatorium.nurse', login_url='logout')
def final_appointment_view(request, pk):

    ill_his = get_object_or_404(IllnessHistory.objects.select_related('patient', 'booking'), pk=pk)

    final_app_instance = FinalAppointmentWithDoctorModel.objects.filter(illness_history=ill_his)

    if final_app_instance:
        final_app_form = FinalAppointmentShortForm(request.POST, instance=final_app_instance.first())
    else:
        final_app_form = FinalAppointmentShortForm(request.POST)

    context = assemble_context(ill_his)
    context.update({
        'final_app_form': final_app_form,
        'treatment_results_choices': FinalAppointmentWithDoctorModel.treatment_results.field.choices,
    })

    return render(request, 'sanatorium/nurse/appointments/final_appointment.html', context)


@role_required(role='sanatorium.nurse', login_url='logout')
def cardiologist_appointment_view(request, pk):

    ill_his = get_object_or_404(IllnessHistory.objects.select_related('patient', 'booking'), pk=pk)

    cardiologist_app_instance = ConsultingWithCardiologistModel.objects.filter(illness_history=ill_his).first()

    context = assemble_context(ill_his)

    cardiologist_app_form = ConsultingWithCardiologistShortForm(instance=cardiologist_app_instance)

    context['cardiologist_app_form'] = cardiologist_app_form
    context['state_choices'] = ConsultingWithCardiologistModel.state.field.choices

    return render(request, 'sanatorium/nurse/appointments/cardiologist_appointment.html', context)


@role_required(role='sanatorium.nurse', login_url='logout')
def neurologist_appointment_view(request, pk):

    ill_his = get_object_or_404(IllnessHistory.objects.select_related('patient', 'booking'), pk=pk)

    neurologist_app_instance = ConsultingWithNeurologistModel.objects.filter(illness_history=ill_his).first()

    context = assemble_context(ill_his)

    neurologist_app_form = ConsultingWithNeurologistShortForm(instance=neurologist_app_instance)

    context['neurologist_app_form'] = neurologist_app_form
    context['state_choices'] = ConsultingWithNeurologistModel.state.field.choices

    return render(request, 'sanatorium/nurse/appointments/neurologist_appointment.html', context)


@role_required(role='sanatorium.nurse', login_url='logout')
def on_arrival_appointments_view(request, pk):

    ill_his = get_object_or_404(IllnessHistory.objects.select_related('patient', 'booking'), pk=pk)

    on_arrival_app_instance = AppointmentWithOnDutyDoctorOnArrivalModel.objects.filter(illness_history=ill_his).first()

    context = assemble_context(ill_his)

    on_arrival_app_form = AppointmentWithOnDutyDoctorOnArrivalShortForm(instance=on_arrival_app_instance)

    context['on_arrival_app_form'] = on_arrival_app_form
    context['state_choices'] = AppointmentWithOnDutyDoctorOnArrivalModel.state.field.choices

    return render(request, 'sanatorium/nurse/appointments/on_arrival_appointment.html', context)


@role_required(role='sanatorium.nurse', login_url='logout')
def repeated_appointments_view(request, pk):

    ill_his = get_object_or_404(IllnessHistory.objects.select_related('patient', 'booking'), pk=pk)

    context = assemble_context(ill_his)

    repeated_app_form = RepeatedAppointmentWithDoctorShortForm(request.POST or None, request.FILES or None)

    context['repeated_app_form'] = repeated_app_form
    context['state_choices'] = RepeatedAppointmentWithDoctorModel.state.field.choices

    return render(request, 'sanatorium/nurse/appointments/repeated_appointment.html', context)


@role_required(role='sanatorium.nurse', login_url='logout')
def update_repeated_appointments_view(request, pk):

    repeated_app_instance = get_object_or_404(RepeatedAppointmentWithDoctorModel, pk=pk)

    ill_his = repeated_app_instance.illness_history

    context = assemble_context(ill_his)

    repeated_app_form = RepeatedAppointmentWithDoctorShortForm(instance=repeated_app_instance)
    context['repeated_app_form'] = repeated_app_form
    context['state_choices'] = RepeatedAppointmentWithDoctorModel.state.field.choices

    return render(request, 'sanatorium/nurse/appointments/repeated_appointment.html', context)


@role_required(role='sanatorium.nurse', login_url='logout')
def with_doc_on_duty_appointment_view(request, pk):

    ill_his = get_object_or_404(IllnessHistory.objects.select_related('patient', 'booking'), pk=pk)

    with_doc_on_duty_instance = AppointmentWithOnDutyDoctorModel.objects.filter(illness_history=ill_his).first()

    context = assemble_context(ill_his)

    with_doc_on_duty_form = AppointmentWithOnDutyDoctorForm(instance=with_doc_on_duty_instance)

    context['with_doc_on_duty_form'] = with_doc_on_duty_form
    context['state_choices'] = AppointmentWithOnDutyDoctorModel.state.field.choices
    context['for_sanatorium_treatment_choices'] = AppointmentWithOnDutyDoctorModel.for_sanatorium_treatment.field.choices

    return render(request, 'sanatorium/nurse/appointments/with_doc_on_duty_appointment.html', context)


@role_required(role='sanatorium.nurse', login_url='logout')
def update_with_doc_on_duty_appointment_view(request, pk):

    with_doc_on_duty_instance = get_object_or_404(AppointmentWithOnDutyDoctorModel, pk=pk)

    ill_his = with_doc_on_duty_instance.illness_history

    context = assemble_context(ill_his)

    with_doc_on_duty_form = AppointmentWithOnDutyDoctorForm(instance=with_doc_on_duty_instance)
    context['with_doc_on_duty_form'] = with_doc_on_duty_form
    context['state_choices'] = AppointmentWithOnDutyDoctorModel.state.field.choices
    context['for_sanatorium_treatment_choices'] = AppointmentWithOnDutyDoctorModel.for_sanatorium_treatment.field.choices

    return render(request, 'sanatorium/nurse/appointments/with_doc_on_duty_appointment.html', context)


@role_required(role='sanatorium.nurse', login_url='logout')
def ekg_appointment_view(request, pk):

    ill_his = get_object_or_404(IllnessHistory.objects.select_related('patient', 'booking'), pk=pk)

    ekg_instance = EkgAppointmentModel.objects.filter(illness_history=ill_his).first()

    context = assemble_context(ill_his)

    ekg_form = EkgAppointmentShortForm(instance=ekg_instance)

    context['ekg_form'] = ekg_form
    context['state_choices'] = EkgAppointmentModel.state.field.choices
    context['for_sanatorium_treatment_choices'] = EkgAppointmentModel.for_sanatorium_treatment.field.choices

    return render(request, 'sanatorium/nurse/appointments/ekg_appointment.html', context)


@role_required(role='sanatorium.nurse', login_url='logout')
def update_ekg_appointment_view(request, pk):

    ekg_instance = get_object_or_404(EkgAppointmentModel, pk=pk)

    ill_his = ekg_instance.illness_history

    context = assemble_context(ill_his)

    ekg_form = EkgAppointmentShortForm(instance=ekg_instance)
    context['ekg_form'] = ekg_form
    context['state_choices'] = EkgAppointmentModel.state.field.choices
    context['for_sanatorium_treatment_choices'] = EkgAppointmentModel.for_sanatorium_treatment.field.choices

    return render(request, 'sanatorium/nurse/appointments/ekg_appointment.html', context)