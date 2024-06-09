from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from apps.warehouse.forms import ItemForm
from apps.warehouse.models import ItemsModel, WarehouseChequeModel


def main_screen_view(request):
    return render(request, 'v2/main_point/mainsreen.html', context={})


def search_items(request):
    if request.is_ajax() and 'term' in request.GET:
        qs = ItemsModel.objects.filter(name__istartswith=request.GET.get('term'))
        items = list(qs.values('id', 'name'))
        return JsonResponse(items, safe=False)
    return render(request, 'v2/main_point/income2.html')


def search_items(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and 'term' in request.GET:
        term = request.GET.get('term')
        qs = ItemsModel.objects.filter(name__istartswith=term)
        items = list(qs.values('id', 'name'))
        return JsonResponse(items, safe=False)
    return render(request, 'v2/main_point/income2.html')


def item_list(request):
    if request.method == 'POST':
        formset = ItemForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('item_list')
    else:
        formset = ItemForm()

    return render(request, 'v2/main_point/test.html', {'formset': formset})


def cheque_view(request):
    cheques = WarehouseChequeModel.objects.all()
    context = {
        "cheques": cheques
    }
    return render(request, 'v2/cheque/cheque_list.html', context)


def cheque_detailed_view(request, pk):
    cheque = get_object_or_404(WarehouseChequeModel, pk=pk)
    context = {
        "cheque": cheque,
        "details": cheque.cheque_items.all()
    }
    return render(request, 'v2/cheque/cheque_details.html', context)
