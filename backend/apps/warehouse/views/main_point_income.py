from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from apps.warehouse.forms import ItemForm
from apps.warehouse.models import ItemsModel, WarehouseChequeModel
from apps.warehouse.models.store_point import StorePointStaffModel


@login_required
def main_screen_view(request):
    staff = request.user
    store_point = StorePointStaffModel.objects.filter(staff=staff)
    print(store_point)
    if not store_point:
        return redirect('warehouse_v2:logout')

    store_point = store_point.first()
    if store_point.store_point.is_main:
        return render(request, 'main_screen/main_screen.html', context={})
    else:
        return render(request, 'main_screen/main_screen.html', context={})


