from django.shortcuts import render

from apps.warehouse.models import ItemsInStockModel


def items_list_view(request):
    items = ItemsInStockModel.objects.all()
    context = {
        "items": items
    }
    return render(request, 'v2/items/items_list.html', context=context)
