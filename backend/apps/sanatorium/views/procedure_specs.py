import datetime
from operator import attrgetter

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from apps.account.models import DoctorAccountModel
from apps.decorators import role_required
from apps.sanatorium.forms.procedure_specs import ProcedureDaysStatusForm
from apps.sanatorium.models import ProcedureDaysModel


PROCEDURES_PER_PAGE = 30


@role_required(role='sanatorium.procedure_specs', login_url='logout')
def get_assigned_procedures(request):
    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')

    doctor_account = DoctorAccountModel.objects.filter(doctor=request.user).first()

    if search_query:
        procedures = sorted(get_procedures_queryset(search_query, doctor_account), key=attrgetter('start_at'), reverse=True)
    else:
        procedures = sorted(get_procedures_queryset(query, doctor_account), key=attrgetter('start_at'), reverse=True)

    procedures = paginate_procedures(request, procedures)

    context = {
        "procedures": procedures,
        "today": datetime.date.today()
    }

    return render(request, 'sanatorium/procedure_specs/main_screen.html', context)


@role_required(role='sanatorium.procedure_specs', login_url='logout')
def get_all_procedures(request):

    doctor_account = DoctorAccountModel.objects.filter(doctor=request.user).first()

    procedures = sorted(ProcedureDaysModel.objects.filter(procedure_doctor=doctor_account), key=attrgetter('start_at'), reverse=True)

    procedures = paginate_procedures(request, procedures)

    context = {
        "all_procedures": True,
        "procedures": procedures,
        "today": datetime.date.today()
    }

    return render(request, 'sanatorium/procedure_specs/main_screen.html', context)


@role_required(role='sanatorium.procedure_specs', login_url='logout')
def get_procedures_by_start_date_view(request):
    start_date_str = request.GET.get('start_date')

    return get_procedures_by_date_view(request, start_date_str)


def get_procedures_by_date_view(request, end_date):
    start_date_str = request.GET.get('start_date')

    procedures = ProcedureDaysModel.objects.filter(start_at__date=end_date)

    procedures_data = [{
        'id': procedure.id,
        'state': procedure.state,
        'patient_full_name': procedure.procedure.illness_history.patient.full_name,
        'procedure': procedure.procedure.medical_service.name,
        'procedure_doctor': procedure.procedure_doctor.doctor.full_name,
        'is_out_of_graphic': procedure.is_out_of_graphic,
    } for procedure in procedures]

    return JsonResponse({'procedures': procedures_data})


@role_required(role='sanatorium.procedure_specs', login_url='logout')
def update_procedure_state_view(request, pk):
    next_url = request.GET.get('next')

    procedures = ProcedureDaysModel.objects.filter(pk=pk).first()
    if not procedures:
        return redirect('sanatorium_procedure_specs:main_screen')
    if request.method == 'POST':
        form = ProcedureDaysStatusForm(request.POST, instance=procedures)
        if form.is_valid():
            target_object = form.save(commit=False)
            target_object.updated_by = request.user
            target_object.save()
            return redirect(next_url if next_url else 'sanatorium_procedure_specs:main_screen')
        print(form.errors)

    form = ProcedureDaysStatusForm(instance=procedures)

    state_choices = ["отменено", "выполнено"]

    context = {
        'form': form,
        'state_choices': state_choices,
    }
    return render(request, 'sanatorium/procedure_specs/update_procedure_state.html', context)


@role_required(role='sanatorium.procedure_specs', login_url='logout')
def make_it_done_procedure_state_view(request, pk):
    next_url = request.GET.get('next')

    procedures = ProcedureDaysModel.objects.filter(pk=pk).first()
    if not procedures:
        return redirect('sanatorium_procedure_specs:main_screen')

    procedures.state = 'выполнено'
    procedures.updated_by = request.user
    procedures.save()

    return redirect(next_url if next_url else 'sanatorium_procedure_specs:main_screen')


def paginate_procedures(request, procedures):
    page = request.GET.get('page', 1)
    procedures_paginator = Paginator(procedures, PROCEDURES_PER_PAGE)

    try:
        procedures = procedures_paginator.page(page)
    except PageNotAnInteger:
        procedures = procedures_paginator.page(PROCEDURES_PER_PAGE)
    except EmptyPage:
        procedures = procedures_paginator.page(procedures_paginator.num_pages)

    return procedures


def get_procedures_queryset(query=None, doctor=None):
    queryset = []
    queries = query.split(" ")

    today_date = datetime.date.today()

    for q in queries:
        procedures = (ProcedureDaysModel.objects.filter(start_at__date=today_date).filter(procedure_doctor=doctor).filter(
            Q(procedure__illness_history__series_number__icontains=q) |
            Q(procedure__illness_history__patient__f_name__icontains=q) |
            Q(procedure__illness_history__patient__mid_name__icontains=q)
        ).distinct())
        for new in procedures:
            queryset.append(new)

    return list(set(queryset))