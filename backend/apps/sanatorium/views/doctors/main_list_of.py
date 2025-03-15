from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render

from apps.account.models import DoctorAccountModel, NurseAccountModel, MedicalService
from apps.decorators import role_required
from apps.lis.models import LabResearchModel, LabResearchCategoryModel
from apps.logus.models import AvailableTariffModel, AvailableRoomModel, AvailableRoomsTypeModel
from apps.sanatorium.forms.doctors import BasePillsInjectionsForm, BaseProcedureServiceForm, BaseLabResearchServiceForm, \
    LabResultForm
from apps.sanatorium.models import IllnessHistory, BasePillsInjectionsModel, BaseProcedureServiceModel, \
    BaseLabResearchServiceModel, LabResult
from apps.sanatorium.views.doctors.appointments import assemble_context, get_all_appointments
from apps.warehouse.models import ItemsInStockModel, ChequeItemsModel

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

        'pills': ItemsInStockModel.objects.filter(warehouse__is_main=True),
        'pill_frequency_types': ChequeItemsModel.frequency.field.choices,
        'assigned_pills': ChequeItemsModel.objects.filter(cheque__illness_history=ill_his),
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

    item_update = get_object_or_404(ChequeItemsModel, pk=pk)
    next_url = request.GET.get('next', '')

    if request.method == "POST":
        form = BasePillsInjectionsForm(request.POST, instance=item_update)
        if form.is_valid():
            item: ChequeItemsModel = form.save(commit=False)
            item.modified_by = request.user
            item.save()
            if next_url:
                return redirect(next_url)
            return redirect("sanatorium_doctors:main_list_of_procedures", pk=item_update.cheque.illness_history.pk)
        else:
            context = {
                'form': form,
                'pills': ItemsInStockModel.objects.filter(warehouse__is_main=True),
                'pill_frequency_types': ChequeItemsModel.frequency.field.choices,
                'ill_his': item_update.cheque.illness_history,
                'next': next_url,
            }
            return render(request, "sanatorium/doctors/pills_injections_update.html", context)
    else:
        form = BasePillsInjectionsForm(instance=item_update)

    context = {
        'form': form,
        'pills': ItemsInStockModel.objects.filter(warehouse__is_main=True),
        'pill_frequency_types': ChequeItemsModel.frequency.field.choices,
        'ill_his': item_update.cheque.illness_history,
        'next': next_url,
    }
    return render(request, "sanatorium/doctors/pills_injections_update.html", context)


@role_required(role='sanatorium.doctor', login_url='logout')
def pills_injections_delete(request, pk):

    item_delete= get_object_or_404(ChequeItemsModel, pk=pk)
    return_pk = item_delete.cheque.illness_history.pk
    next_url = request.GET.get('next', '')

    if request.method == "POST":
        item_delete.delete()
        if next_url:
            return redirect(next_url)
    return redirect("sanatorium_doctors:main_list_of_procedures", pk=return_pk)


@role_required(role='sanatorium.doctor', login_url='logout')
def consulting_update(request, pk):

    item_update = get_object_or_404(BaseLabResearchServiceModel, pk=pk)
    next_url = request.GET.get('next', '')

    context = assemble_context(item_update.illness_history)
    context.update({
        'lab_results': item_update.lab_results.all(),
    })

    if request.method == "POST":
        form = BaseLabResearchServiceForm(request.POST, instance=item_update)
        lab_result_form = LabResultForm(request.POST, request.FILES)
        if form.is_valid():
            item: BaseLabResearchServiceModel = form.save(commit=False)
            item.modified_by = request.user
            item.save()
            if next_url:
                return redirect(next_url)
            return redirect("sanatorium_doctors:main_list_of_procedures", pk=item_update.illness_history.pk)
        if 'lab_result_form' in request.POST and lab_result_form.is_valid():
            lab_result: LabResult = lab_result_form.save(commit=False)
            lab_result.created_by = request.user
            lab_result.base_lab_research = item_update
            lab_result.save()
            return redirect("sanatorium_doctors:consulting_update", pk=pk)
        else:
            context.update({
                'active_page': {'proc_main_list_page': 'active'},
                'form': form,
                'labs': LabResearchModel.objects.all(),
                'labs_types': LabResearchCategoryModel.objects.all(),
                'ill_his': item_update.illness_history,
                'next': next_url,
            })
            return render(request, "sanatorium/doctors/consultings_update.html", context)
    else:
        form = BaseLabResearchServiceForm(instance=item_update)

    context.update({
        'active_page': {'proc_main_list_page': 'active'},
        'form': form,
        'labs': LabResearchModel.objects.all(),
        'labs_types': LabResearchCategoryModel.objects.all(),
        'ill_his': item_update.illness_history,
        'next': next_url,
    })
    return render(request, "sanatorium/doctors/consultings_update.html", context)


@role_required(role='sanatorium.doctor', login_url='logout')
def consulting_result_update(request, pk):

    item_update = get_object_or_404(LabResult, pk=pk)
    next_url = request.GET.get('next', '')

    context = assemble_context(item_update.base_lab_research.illness_history)

    if request.method == "POST":
        form = LabResultForm(request.POST, request.FILES, instance=item_update)
        if form.is_valid():
            item: LabResult = form.save(commit=False)
            item.modified_by = request.user
            item.save()
            if next_url:
                return redirect(next_url)
            return redirect("sanatorium_doctors:main_list_of_procedures", pk=item_update.base_lab_research.illness_history.pk)
        else:
            context.update({
                'active_page': {'proc_main_list_page': 'active'},
                'form': form,
                'labs': LabResearchModel.objects.all(),
                'labs_types': LabResearchCategoryModel.objects.all(),
                'ill_his': item_update.base_lab_research.illness_history,
                'next': next_url,
            })
            return render(request, "sanatorium/doctors/consulting_result_update.html", context)
    else:
        form = LabResultForm(instance=item_update)

    context.update({
        'active_page': {'proc_main_list_page': 'active'},
        'form': form,
        'labs': LabResearchModel.objects.all(),
        'ill_his': item_update.base_lab_research.illness_history,
        'next': next_url,
    })
    return render(request, "sanatorium/doctors/consulting_result_update.html", context)


@role_required(role='sanatorium.doctor', login_url='logout')
def consulting_result_delete(request, pk):
    next_url = request.GET.get('next', '')

    result = get_object_or_404(LabResult, pk=pk)
    redirect_url_pk = result.base_lab_research.illness_history.pk
    result.delete()
    if next_url:
        return redirect(next_url)
    return redirect("sanatorium_doctors:consulting_update", pk=redirect_url_pk)


@role_required(role='sanatorium.doctor', login_url='logout')
def get_patient_lab_research_view(request, pk):

    target_lab = get_object_or_404(BaseLabResearchServiceModel, pk=pk)
    lab_results = target_lab.lab_results.all()
    next_url = request.GET.get('next', '')

    context = assemble_context(target_lab.illness_history)

    context.update({
        'active_page': {'proc_main_list_page': 'active'},
        'assigned_lab': target_lab,
        'lab_results': lab_results,
        'next': next_url,
    })
    return render(request, "sanatorium/doctors/patient_lab_research_detail.html", context)


@role_required(role='sanatorium.doctor', login_url='logout')
def update_lab_research_result_view(request, pk):

    target_lab_result = get_object_or_404(LabResult, pk=pk)
    next_url = request.GET.get('next', '')

    context = get_all_appointments(target_lab_result.base_lab_research.illness_history)

    context.update({
        'active_page': {'proc_main_list_page': 'active'},
        'lab_result': target_lab_result,
        'next': next_url,
    })
    return render(request, "sanatorium/doctors/patient_lab_research_result_update.html", context)