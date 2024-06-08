from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from apps.warehouse.forms import AccountAuthenticationForm
from django.contrib.auth import authenticate, login, logout
from apps.account.models import OrganizationModel
from apps.warehouse.models import ItemsModel, ItemsInStockModel, ReceivedItemsModel, IncomeModel, ReceiveRegistryModel, \
    SendRegistryModel, StorePointModel


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
    return render(request, 'v2/auth/login.html', context)
