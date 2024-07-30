import datetime
from operator import attrgetter

from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from apps.warehouse.forms.cheque import ChequeItemCountForm
from apps.warehouse.models import WarehouseChequeModel, ChequeItemsModel, ItemsInStockModel

ITEMS_PER_PAGE = 30


def cheque_view(request):
    query = request.GET.get('q', '')
    print(f"q: {query}")
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


@login_required
def cheque_item_count_update(request, pk, quantity):
    cheque_item = get_object_or_404(ChequeItemsModel, pk=pk)
    if not cheque_item.quantity == quantity:
        cheque_item.quantity = quantity
        cheque_item.modified_at = datetime.datetime.now()
        cheque_item.modified_by = request.user
        cheque_item.save(update_fields=["quantity", "modified_at", "modified_by"])
    return redirect("warehouse_v2:cheque-detailed", pk=cheque_item.cheque.pk)


import json


@login_required
def add_item_to_cheque(request, ):
    data = json.loads(request.body)
    pk = data.get('id')
    quantity = data.get('quantity')
    cheque_pk = data.get('cheque')
    item = get_object_or_404(ItemsInStockModel, pk=pk)
    cheque = get_object_or_404(WarehouseChequeModel, pk=cheque_pk)
    ChequeItemsModel.objects.create(cheque=cheque, item=item, quantity=quantity, created_by=request.user,
                                    modified_by=request.user)
    return JsonResponse({}, status=200)


@login_required
def cheque_item_detailed_view(request, pk):
    context = {}
    cheque_item = get_object_or_404(ChequeItemsModel, pk=pk)
    if request.method == "GET":
        form = ChequeItemCountForm(instance=cheque_item)
        context["form"] = form
        context["item_name"] = cheque_item.item.item.name
        context["price"] = cheque_item.price
    elif request.method == "POST":
        form = ChequeItemCountForm(request.POST, instance=cheque_item)
        if form.is_valid():
            cheque_item: ChequeItemsModel = form.save(commit=False)
            cheque_item.modified_by = request.user
            cheque_item.modified_at = datetime.datetime.now()
            cheque_item.save()
            return redirect("warehouse_v2:cheque-detailed", pk=cheque_item.cheque.pk)
    return render(request, "cheque/cheque_item_update.html", context)


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
