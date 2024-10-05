from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render

from apps.account.models import PatientModel, DoctorAccountModel, NurseAccountModel, MedicalService
from apps.decorators import role_required
from apps.lis.models import LabResearchModel, LabResearchCategoryModel
from apps.logus.models import BookingModel, AvailableTariffModel, AvailableRoomModel, AvailableRoomsTypeModel
from apps.sanatorium.forms.doctors import BasePillsInjectionsForm, BaseProcedureServiceForm, BaseLabResearchServiceForm
from apps.sanatorium.forms.patient import PatientUpdateForm, BookingModelUpdateForm, IllnessHistoryUpdateForm
from apps.sanatorium.models import IllnessHistory, BasePillsInjectionsModel, BaseProcedureServiceModel, \
    BaseLabResearchServiceModel
from apps.warehouse.models import ItemsInStockModel
from urllib.parse import urlencode

BOOKINGS_PER_PAGE = 30


@role_required(role='sanatorium.doctor', login_url='logout')
def main_list_of_procedures_view(request, pk):

    ill_his = get_object_or_404(IllnessHistory.objects.select_related('patient', 'booking'), pk=pk)

    if request.method == "POST":

        pills_form = BasePillsInjectionsForm(request.POST)
        procedures_form = BaseProcedureServiceForm(request.POST)
        lab_research_form = BaseLabResearchServiceForm(request.POST)

        if 'pills_form' in request.POST and pills_form.is_valid():
            pills_injections: BasePillsInjectionsModel = pills_form.save(commit=False)
            pills_injections.modified_by = request.user
            pills_injections.created_by = request.user
            pills_injections.illness_history = ill_his
            pills_injections.save()
            return redirect('sanatorium_doctors:main_list_of_procedures', pk=pk)
        if 'procedures_form' in request.POST and procedures_form.is_valid():
            procedures: BaseProcedureServiceModel = procedures_form.save(commit=False)
            procedures.modified_by = request.user
            procedures.created_by = request.user
            procedures.illness_history = ill_his
            procedures.save()
            return redirect('sanatorium_doctors:main_list_of_procedures', pk=pk)
        if 'lab_research_form' in request.POST and lab_research_form.is_valid():
            lab_research: BaseLabResearchServiceModel = lab_research_form.save(commit=False)
            lab_research.modified_by = request.user
            lab_research.created_by = request.user
            lab_research.illness_history = ill_his
            lab_research.save()
            return redirect('sanatorium_doctors:main_list_of_procedures', pk=pk)

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


@role_required(role='sanatorium.doctor', login_url='logout')
def treatment_procedure_update(request, pk):

    item_update = get_object_or_404(BaseProcedureServiceModel, pk=pk)
    next_url = request.GET.get('next', '')

    if request.method == "POST":
        form = BaseProcedureServiceForm(request.POST, instance=item_update)
        if form.is_valid():
            item: BaseProcedureServiceModel = form.save(commit=False)
            item.modified_by = request.user
            item.save()
            if next_url:
                return redirect(next_url)
            return redirect("sanatorium_doctors:main_list_of_procedures", pk=item_update.illness_history.pk)
        else:
            print(form.errors)
            # Return the user to the form with errors highlighted
            context = {
                'form': form,
                'procedures_frequency_types': BaseProcedureServiceModel.frequency.field.choices,
                'procedures': MedicalService.objects.filter(type='procedure'),
                'ill_his': item_update.illness_history,
                'next': next_url,
            }
            return render(request, "sanatorium/doctors/treatment_procedures_update.html", context)
    else:
        form = BaseProcedureServiceForm(instance=item_update)

    context = {
        'form': form,
        'procedures_frequency_types': BaseProcedureServiceModel.frequency.field.choices,
        'procedures': MedicalService.objects.filter(type='procedure'),
        'ill_his': item_update.illness_history,
        'next': next_url,
    }

    return render(request, "sanatorium/doctors/treatment_procedures_update.html", context)


@role_required(role='sanatorium.doctor', login_url='logout')
def pills_injections_update(request, pk):

    item_update = get_object_or_404(BasePillsInjectionsModel, pk=pk)
    next_url = request.GET.get('next', '')

    if request.method == "POST":
        form = BasePillsInjectionsForm(request.POST, instance=item_update)
        if form.is_valid():
            item: BasePillsInjectionsModel = form.save(commit=False)
            item.modified_by = request.user
            item.save()
            if next_url:
                return redirect(next_url)
            return redirect("sanatorium_doctors:main_list_of_procedures", pk=item_update.illness_history.pk)
        else:
            context = {
                'form': form,
                'pills': ItemsInStockModel.objects.filter(warehouse__name='Госпиталь'),
                'pill_frequency_types': BasePillsInjectionsModel.frequency.field.choices,
                'ill_his': item_update.illness_history,
                'next': next_url,
            }
            return render(request, "sanatorium/doctors/pills_injections_update.html", context)
    else:
        form = BasePillsInjectionsForm(instance=item_update)

    context = {
        'form': form,
        'pills': ItemsInStockModel.objects.filter(warehouse__name='Gospital'),
        'pill_frequency_types': BasePillsInjectionsModel.frequency.field.choices,
        'ill_his': item_update.illness_history,
        'next': next_url,
    }
    return render(request, "sanatorium/doctors/pills_injections_update.html", context)


@role_required(role='sanatorium.doctor', login_url='logout')
def consulting_update(request, pk):

    item_update = get_object_or_404(BaseLabResearchServiceModel, pk=pk)
    next_url = request.GET.get('next', '')

    if request.method == "POST":
        form = BaseLabResearchServiceForm(request.POST, instance=item_update)
        if form.is_valid():
            item: BaseLabResearchServiceModel = form.save(commit=False)
            item.modified_by = request.user
            item.save()
            if next_url:
                return redirect(next_url)
            return redirect("sanatorium_doctors:main_list_of_procedures", pk=item_update.illness_history.pk)
        else:
            context = {
                'form': form,
                'labs': LabResearchModel.objects.all(),
                'labs_types': LabResearchCategoryModel.objects.all(),
                'ill_his': item_update.illness_history,
                'next': next_url,
            }
            print(form.errors)
            return render(request, "sanatorium/doctors/consultings_update.html", context)
    else:
        form = BaseLabResearchServiceForm(instance=item_update)

    context = {
        'form': form,
        'labs': LabResearchModel.objects.all(),
        'labs_types': LabResearchCategoryModel.objects.all(),
        'ill_his': item_update.illness_history,
        'next': next_url,
    }
    return render(request, "sanatorium/doctors/consultings_update.html", context)