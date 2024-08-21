from operator import attrgetter

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from apps.warehouse.forms.manual.items import ItemsModelCreateForm
from apps.warehouse.models import ItemsModel, CompanyModel

ITEMS_PER_PAGE = 30


@login_required
def items_get_view(request):
    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')
    if search_query:
        items = sorted(get_items_queryset(search_query), key=attrgetter('created_at'), reverse=True)
    else:
        items = sorted(get_items_queryset(query), key=attrgetter('created_at'), reverse=True)

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
    return render(request, "manual/items_list.html", context)


@login_required
def item_create(request):

    if request.method == "POST":
        form = ItemsModelCreateForm(request.POST)
        if form.is_valid():
            item: ItemsModel = form.save(commit=False)
            item.created_by = request.user
            item.modified_by = request.user
            item.save()
            return redirect("warehouse_manual:items")
    context = {}
    form = ItemsModelCreateForm()
    context["form"] = form
    context['companies'] = CompanyModel.objects.all()
    return render(request, "manual/item_create.html", context)


@login_required
def item_update(request, pk):

    item_update = get_object_or_404(ItemsModel, pk=pk)
    if request.method == "POST":
        form = ItemsModelCreateForm(request.POST, instance=item_update)
        if form.is_valid():
            item: ItemsModel = form.save(commit=False)
            item.modified_by = request.user
            item.save()
            return redirect("warehouse_manual:items")
    context = {}
    form = ItemsModelCreateForm(
        initial={
            'company': item_update.company,
            'in_pack': item_update.in_pack,
            'name': item_update.name,
            'unit': item_update.unit,
            'seria': item_update.seria,
        }
    )
    context["form"] = form
    context['companies'] = CompanyModel.objects.all()
    return render(request, "manual/item_update.html", context)


@login_required
def item_delete(request, pk):
    item = get_object_or_404(ItemsModel, pk=pk)
    item.delete()
    return redirect("warehouse_manual:items")


def get_items_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        items = ItemsModel.objects.filter(
                Q(seria__icontains=q) |
                Q(company__name__icontains=q) |
                Q(name__icontains=q)
            ).distinct()
        for new in items:
            queryset.append(new)

    return list(set(queryset))
