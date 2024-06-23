from operator import attrgetter

from django.core.paginator import EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from apps.warehouse.models import WarehouseChequeModel

ITEMS_PER_PAGE = 30


def cheque_view(request):
    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')
    if search_query:
        cheques = sorted(get_cheques_queryset(search_query), key=attrgetter('created_at'), reverse=True)
    else:
        cheques = sorted(get_cheques_queryset(query), key=attrgetter('created_at'), reverse=True)

    page = request.GET.get('page', 1)
    cheques_paginator = Paginator(cheques, ITEMS_PER_PAGE)

    try:
        cheques = cheques_paginator.page(page)
    except PageNotAnInteger:
        cheques = cheques_paginator.page(ITEMS_PER_PAGE)
    except EmptyPage:
        cheques = cheques_paginator.page(cheques_paginator.num_pages)
    context = {
        "cheques": cheques
    }
    return render(request, 'cheque/cheque_list.html', context)


def cheque_detailed_view(request, pk):
    cheque = get_object_or_404(WarehouseChequeModel, pk=pk)
    context = {
        "cheque": cheque,
        "details": cheque.cheque_items.all()
    }
    return render(request, 'cheque/cheque_details.html', context)


def get_cheques_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        cheques = WarehouseChequeModel.objects.filter(
                Q(cheque_number__icontains=q)
            ).distinct()
        for new in cheques:
            queryset.append(new)

    return list(set(queryset))