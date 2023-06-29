from django.contrib.auth.decorators import login_required
from django.db.models import Q, F
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from apps.warehouse.forms import AccountAuthenticationForm
from django.contrib.auth import authenticate, login, logout
from apps.account.models import OrganizationModel
from apps.warehouse.models import ItemsModel, ItemsInStockModel

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
    print(request.POST)
    context["orgs"] = orgs
    return render(request, 'warehouse/index.html', context)


class IncomeView(TemplateView):
    template_name = 'warehouse/income.html'


@login_required
def medicines_view(request, pk=None):
    print(pk)
    context = {}
    items = ItemsModel.objects.all()
    context["items"] = items
    return render(request, 'warehouse/medicines.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('warehouse:warehouse-login')
