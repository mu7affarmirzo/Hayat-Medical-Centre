from itertools import chain
from operator import attrgetter

from django.db.models import Q

from django.core.paginator import EmptyPage, PageNotAnInteger


from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect

from apps.warehouse.forms import ItemSearchForm
from apps.warehouse.models import ItemsModel, ItemsInStockModel, StorePointStaffModel, StorePointModel

ITEMS_PER_PAGE = 30


@login_required
def emergency_items_view(request):
    user = request.user
    warehouse = StorePointModel.objects.filter(is_emergency=True).first()

    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')
    if search_query:
        items = sorted(get_items_queryset(search_query, warehouse), key=attrgetter('item.name'), reverse=True)
    else:
        items = sorted(get_items_queryset(query, warehouse), key=attrgetter('item.name'), reverse=True)

    page = request.GET.get('page', 1)
    items_paginator = Paginator(items, ITEMS_PER_PAGE)

    try:
        items = items_paginator.page(page)
    except PageNotAnInteger:
        items = items_paginator.page(ITEMS_PER_PAGE)
    except EmptyPage:
        items = items_paginator.page(items_paginator.num_pages)

    context = {
        "items": items
    }
    return render(request, 'items/items_list.html', context=context)


def get_items_queryset(query=None, warehouse=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        items = ItemsInStockModel.objects.filter(warehouse=warehouse).filter(
                Q(item__name__icontains=q) |
                Q(income_seria__icontains=q) |
                Q(item__seria__icontains=q)
            ).distinct()
        for new in items:
            queryset.append(new)

    return list(set(queryset))
