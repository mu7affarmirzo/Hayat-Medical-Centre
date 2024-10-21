import datetime
from operator import attrgetter

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render

from apps.account.models import DoctorAccountModel
from apps.decorators import role_required
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

    page = request.GET.get('page', 1)
    procedures_paginator = Paginator(procedures, PROCEDURES_PER_PAGE)

    try:
        procedures = procedures_paginator.page(page)
    except PageNotAnInteger:
        procedures = procedures_paginator.page(PROCEDURES_PER_PAGE)
    except EmptyPage:
        procedures = procedures_paginator.page(procedures_paginator.num_pages)

    context = {
        "procedures": procedures,
        "today": datetime.date.today()
    }

    print(procedures)

    return render(request, 'sanatorium/procedure_specs/main_screen.html', context)



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