from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from apps.warehouse.forms import AddItemToChequeForm
from django.contrib.auth import authenticate, login, logout
from apps.account.models import OrganizationModel
from apps.warehouse.models import ItemsModel, ItemsInStockModel, ReceivedItemsModel, IncomeModel, ReceiveRegistryModel, \
    WarehouseChequeModel, ChequeItemsModel


class ChequeView(TemplateView):
    template_name = 'cheque/F-kassa-new-checks.html'


@login_required
def cheque_list_view(request):
    pass


@login_required
def create_cheque_view(request):
    context = {}
    user = request.user
    cheque = WarehouseChequeModel.objects.create(created_by=user)
    context['cheque'] = cheque
    return redirect('warehouse:cheque-get', pk=cheque.pk)


@login_required
def get_cheque_view(request, pk):
    context = {}
    cheque_items_summa = 0
    user = request.user
    cheque = get_object_or_404(WarehouseChequeModel, pk=pk)
    items = ItemsModel.objects.all()
    cheque_items = ChequeItemsModel.objects.filter(cheque=cheque)
    for i in cheque_items:
        cheque_items_summa += i.quantity * i.item.price
    context['cheque'] = cheque
    context['items'] = items
    context['cheque_items'] = cheque_items
    context['cheque_items_summa'] = cheque_items_summa

    return render(request, 'cheque/F-kassa-new-checks.html', context)


@login_required
@csrf_exempt
def add_item_to_cheque_view(request, ch_pk, i_pk):
    context = {}
    user = request.user
    cheque = get_object_or_404(WarehouseChequeModel, pk=ch_pk)
    item = get_object_or_404(ItemsModel, pk=i_pk)
    cheque_item = ChequeItemsModel.objects.create(cheque=cheque, item=item)
    return redirect('warehouse:cheque-get', pk=cheque.pk)


# @login_required
# @csrf_exempt
# def add_item_to_cheque_view(request, pk):
#     if request.method == 'POST':
#         item_id = request.POST.get('item_id')
#         item = Item.objects.get(id=item_id)
#         # Assuming you have a Cart model and a method to add items.
#         Cart.objects.add_item(item)
#         return JsonResponse({'status': 'success'})
#     else:
#         return JsonResponse({'status': 'fail'})
#
#     context = {}
#     user = request.user
#     cheque = WarehouseChequeModel.objects.create(created_by=user)
#     context['cheque'] = cheque
#     return redirect('warehouse:cheque-get', pk=cheque.pk)

# @login_required
def cheque_popup_view(request, pk):
    cheque = ItemsModel.objects.filter(pk=pk).values("id", "name", "in_stock", "price", "expire_date", "company__name",
                                                     "seria")
    print(cheque)
    return JsonResponse(list(cheque), safe=False)


def cheque_popup_post(request, ch_pk):
    if request.POST:
        form = AddItemToChequeForm(request.POST)
        cheque = get_object_or_404(WarehouseChequeModel, pk=ch_pk)
        print(form.is_valid())
        if form.is_valid():
            itemid = request.POST["itemid"]
            item = get_object_or_404(ItemsModel, pk=itemid)
            quantity = request.POST["quantity"]
            ChequeItemsModel.objects.create(cheque=cheque, quantity=quantity, item=item)
            print(itemid, quantity)
    return redirect("warehouse:cheque-get", ch_pk)
