from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.warehouse.models import SendRegistryModel, StorePointStaffModel


@login_required
def transfers_view(request):
    staff = request.user
    store_point = StorePointStaffModel.objects.filter(staff=staff)

    if not store_point:
        return redirect('warehouse_v2:logout')

    store_point = store_point.first()
    incoming_transfers = SendRegistryModel.objects.filter(receiver=store_point.store_point)
    outgoing_transfers = SendRegistryModel.objects.filter(sender=store_point.store_point)
    context = {
        'incoming_transfers': incoming_transfers,
        'outgoing_transfers': outgoing_transfers,
    }
    return render(request, 'branches/transfers-list.html', context)


@login_required
def transfers_detailed_view(request, pk):
    return render(request, 'branches/transfers-list.html', {})


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