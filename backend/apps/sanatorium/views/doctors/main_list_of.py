from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render

from apps.account.models import PatientModel, DoctorAccountModel, NurseAccountModel, MedicalService
from apps.decorators import role_required
from apps.lis.models import LabResearchModel, LabResearchCategoryModel
from apps.logus.models import BookingModel, AvailableTariffModel, AvailableRoomModel, AvailableRoomsTypeModel
from apps.sanatorium.forms.patient import PatientUpdateForm, BookingModelUpdateForm, IllnessHistoryUpdateForm
from apps.sanatorium.models import IllnessHistory, BasePillsInjectionsModel, BaseProcedureServiceModel, \
    BaseLabResearchServiceModel
from apps.warehouse.models import ItemsInStockModel

BOOKINGS_PER_PAGE = 30


@role_required(role='sanatorium.doctor', login_url='logout')
def main_list_of_procedures_view(request, pk):

    ill_his = get_object_or_404(IllnessHistory.objects.select_related('patient', 'booking'), pk=pk)

    if request.method == "POST":
        forms_mapping = {
            'patient_form': PatientUpdateForm(request.POST, instance=ill_his.patient),
            'ih_form': IllnessHistoryUpdateForm(request.POST, instance=ill_his),
            'booking_form': BookingModelUpdateForm(request.POST, instance=ill_his.booking)
        }

        form_name = next((key for key in forms_mapping if key in request.POST), None)

        if form_name and forms_mapping[form_name].is_valid():
            obj = forms_mapping[form_name].save(commit=False)
            obj.modified_by = request.user
            obj.save()
            if form_name == 'ih_form':
                forms_mapping[form_name].save_m2m()
            return redirect('sanatorium_doctors:title_page', pk=pk)

    context = {
        "active_page": {'proc_main_list_page': 'active'},
        'ill_his': ill_his,
        'ill_his_types': IllnessHistory.type.field.choices,
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

    return render(request, 'sanatorium/doctors/main_list_of_procedures.html', context)
