from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from apps.warehouse.forms import ItemForm
from apps.warehouse.models import ItemsModel, WarehouseChequeModel


def main_screen_view(request):
    return render(request, 'main_point/mainsreen.html', context={})



