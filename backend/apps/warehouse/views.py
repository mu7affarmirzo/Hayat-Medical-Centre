from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from apps.warehouse.forms import AccountAuthenticationForm
from django.contrib.auth import authenticate, login, logout
from apps.account.models import OrganizationModel

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
    print("started")
    if user.is_authenticated:
        return redirect("warehouse:warehouse-index")
    print("asdf")
    print(request.POST)
    if request.POST:
        print("request.POST")
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            print(email, password)
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("warehouse:warehouse-index")
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'warehouse/login.html', context)


@login_required
def index_view(request):
    context = {}
    orgs = OrganizationModel.objects.all()
    context["orgs"] = orgs
    return render(request, 'warehouse/index.html', context)


class IncomeView(TemplateView):
    template_name = 'warehouse/income.html'


class MedicinesView(TemplateView):
    template_name = 'warehouse/medicines.html'


@login_required
def logout_view(request):
    logout(request)
    return redirect('warehouse:warehouse-login')
