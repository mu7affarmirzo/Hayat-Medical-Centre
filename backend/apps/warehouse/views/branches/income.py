from operator import attrgetter

from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from apps.account.models import NotificationModel
from apps.warehouse.models import SendRegistryModel
# from apps.warehouse.models.store_point import StorePointStaffModel

ITEMS_PER_PAGE = 30


# @login_required
# def branch_income_view(request):
#     staff = request.user
#     query = request.GET.get('q', '')
#     search_query = request.GET.get('table_search')
#
#     store_point = StorePointStaffModel.objects.filter(staff=staff)
#     if not store_point:
#         return redirect('warehouse_v2:logout')
#
#     store_point = store_point.first()
#
#     if search_query:
#         incomes = sorted(get_transfers_queryset(store_point.store_point, search_query), key=attrgetter('created_at'), reverse=True)
#     else:
#         incomes = sorted(get_transfers_queryset(store_point.store_point, query), key=attrgetter('created_at'), reverse=True)
#
#     page = request.GET.get('page', 1)
#     incomes_paginator = Paginator(incomes, ITEMS_PER_PAGE)
#
#     try:
#         incomes = incomes_paginator.page(page)
#     except PageNotAnInteger:
#         incomes = incomes_paginator.page(ITEMS_PER_PAGE)
#     except EmptyPage:
#         incomes = incomes_paginator.page(incomes_paginator.num_pages)
#
#     context = {
#         "incomes": incomes
#     }
#     notifications = NotificationModel.objects.filter(receiver=request.user, state=False)
#     context['notifications'] = notifications
#
#     return render(request, 'branches/income_list.html', context)


def detailed_income_view(request, pk):
    income = get_object_or_404(SendRegistryModel, pk=pk)
    notifications = NotificationModel.objects.filter(receiver=request.user, state=False)

    context = {
        "income": income,
        "notifications": notifications,
        "details": income.send_registry_items.all()
    }

    return render(request, 'branches/income_details.html', context)


def get_transfers_queryset(store_point, query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        transfers = SendRegistryModel.objects.filter(receiver=store_point).filter(
                Q(series__icontains=q) |
                Q(receiver__name__icontains=q) |
                Q(state__icontains=q)
            ).distinct()
        for new in transfers:
            queryset.append(new)

    return list(set(queryset))