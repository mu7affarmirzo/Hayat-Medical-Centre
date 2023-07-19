from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from apps.warehouse.forms import AccountAuthenticationForm
from django.contrib.auth import authenticate, login, logout
from apps.account.models import OrganizationModel
from apps.warehouse.models import ItemsModel, ItemsInStockModel, ReceivedItemsModel, IncomeModel, ReceiveRegistryModel

# ------------------------------
#           TASKS
# ------------------------------
"""
1. 

"""


# Create your views here.
def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("warehouse:warehouse-recreg")
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("warehouse:warehouse-recreg")
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'warehouse/login.html', context)


@login_required(login_url="warehouse:warehouse-login")
def index_view(request):
    context = {}
    orgs = OrganizationModel.objects.all()
    print(request.POST)
    context["orgs"] = orgs
    return render(request, 'warehouse/index.html', context)


def receive_registry_view(request, pk=None):
    context = {}
    if pk:
        rec_reg_items = get_object_or_404(ReceiveRegistryModel, pk=pk)
        context["rec_reg_items"] = rec_reg_items

    receive_registry = ReceiveRegistryModel.objects.all()
    summa_prices = 0
    for i in receive_registry:
        summa_prices += i.summa_prices
    context["receive_registry"] = receive_registry
    context["summa_prices"] = summa_prices

    return render(request, 'warehouse/receive_registry.html', context)


@login_required(login_url="warehouse:warehouse-login")
def medicines_view(request, pk=None):
    context = {}
    if pk:
        item = get_object_or_404(ItemsModel, pk=pk)
        received_items = ReceivedItemsModel.objects.filter(item=item)

        context["received_items"] = received_items
    items = ItemsModel.objects.all()
    context["items"] = items
    return render(request, 'warehouse/medicines.html', context)


@login_required(login_url="warehouse:warehouse-login")
def logout_view(request):
    logout(request)
    return redirect('warehouse:warehouse-login')


def incomes_view(request, pk=None):
    context = {}
    if pk:
        income_with_id = get_object_or_404(IncomeModel, pk=pk)
        context["income_with_id"] = income_with_id

    incomes = IncomeModel.objects.all()
    summa_prices = 0
    for i in incomes:
        summa_prices += i.summa_prices
    context["incomes"] = incomes
    context["summa_prices"] = summa_prices

    return render(request, 'warehouse/incomes.html', context)
