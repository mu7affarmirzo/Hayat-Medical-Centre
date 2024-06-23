from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.warehouse.forms import AccountAuthenticationForm
from apps.warehouse.models.store_point import StorePointStaffModel


def user_redirect(user):
    role_page = StorePointStaffModel.objects.filter(staff__in=[user]).first()
    if role_page:
        return redirect(role_page.role.name)
    else:
        return redirect("warehouse_v2:mainscreen")


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return user_redirect(user)
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                # return user_redirect(user)
                return redirect("warehouse_v2:mainscreen")

    form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'auth/login.html', context)


@login_required(login_url="warehouse_v2:login")
def logout_view(request):
    logout(request)
    return redirect('warehouse_v2:login')
