from django.shortcuts import redirect
from operator import attrgetter

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import render

from apps.account.models import DoctorAccountModel
from apps.decorators import role_required
from apps.sanatorium.forms.dispatchers import DispatchBaseProcedureServiceForm
from apps.sanatorium.models import IllnessHistory, BaseProcedureServiceModel, ProcedureDaysModel

procedures_PER_PAGE = 30


@role_required(role='sanatorium.dispatcher', login_url='logout')
def get_waiting_list(request):
    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')

    doctor = DoctorAccountModel.objects.filter(doctor=request.user).first()
    if not doctor:
        return render(request, 'sanatorium/dispatcher/waiting-to-dispatch.html', {})

    if search_query:
        procedures = sorted(get_procedures_to_dispatch(search_query), key=attrgetter('start_date'), reverse=True)
    else:
        procedures = sorted(get_procedures_to_dispatch(query), key=attrgetter('start_date'), reverse=True)

    page = request.GET.get('page', 1)
    procedures_paginator = Paginator(procedures, procedures_PER_PAGE)

    try:
        procedures = procedures_paginator.page(page)
    except PageNotAnInteger:
        procedures = procedures_paginator.page(procedures_PER_PAGE)
    except EmptyPage:
        procedures = procedures_paginator.page(procedures_paginator.num_pages)

    context = {
        "procedures": procedures
    }

    return render(request, 'sanatorium/dispatcher/waiting-to-dispatch.html', context)


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

            days = ProcedureDaysModel.objects.filter(procedure=procedure)
            for day in days:
                day.procedure_doctor = procedure.procedure_doctor
                day.save()

            procedure.save()

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

    return render(request, 'sanatorium/dispatcher/patient_procedure_by_days.html', context)



def get_procedures_to_dispatch(query=None):
    queryset = []
    queries = query.split(" ")

    for q in queries:
        procedures = (BaseProcedureServiceModel.objects.all().exclude(state='state').
                    filter(
            Q(illness_history__series_number__icontains=q) |
            Q(illness_history__patient__f_name__icontains=q) |
            Q(illness_history__patient__mid_name__icontains=q)
        ).distinct())

        for new in procedures:
            queryset.append(new)

    return list(set(queryset))

