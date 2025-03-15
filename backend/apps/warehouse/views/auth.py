from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.account.models import NotificationModel, AccountRolesModel
from apps.warehouse.forms import AccountAuthenticationForm
from apps.warehouse.models.store_point import StorePointStaffModel


USER_ROLE_REDIRECTS = {
    'warehouse': 'warehouse_v2:main_screen',

    'logus.reception': 'logus_auth:main_screen',

    'massage.reception': 'massage_reception:main_screen',

    'sanatorium.staff': 'sanatorium_staff:main_screen',
    'sanatorium.nurse': 'sanatorium_nurse:main_screen',
    'sanatorium.admin': 'sanatorium_admin:main_screen',
    'sanatorium.doctor': 'sanatorium_doctors:main_screen',
    'sanatorium.dispatcher': 'sanatorium_dispatchers:main_screen',
    'sanatorium.procedure_specs': 'sanatorium_procedure_specs:main_screen',
}


def get_redirect_url_for_role(user):
    target_role = AccountRolesModel.objects.filter(user=user).first()
    if target_role:
        role_name = target_role.role.name
        return USER_ROLE_REDIRECTS.get(role_name)
    return None

def user_redirect(user):
    role_page = StorePointStaffModel.objects.filter(staff__in=[user]).first()
    if role_page:
        return redirect(role_page.role.name)
    else:
        return redirect("warehouse_v2:main_screen")


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        redirect_url = get_redirect_url_for_role(user)
        if redirect_url:
            return redirect(redirect_url)
        return render(request, 'auth/login.html', context)

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                redirect_url = get_redirect_url_for_role(user)
                if redirect_url:
                    return redirect(redirect_url)
                return redirect('warehouse_v2:logout')
            else:
                return redirect('login')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'auth/login.html', context)


@login_required(login_url="warehouse_v2:login")
def logout_view(request):
    logout(request)
    return redirect('warehouse_v2:login')


@login_required(login_url="warehouse_v2:login")
def main_screen_view(request):
    context = {}
    staff = request.user
    store_point = StorePointStaffModel.objects.filter(staff=staff)

    if not store_point:
        logout(request)
        return redirect('warehouse_v2:login')

    store_point = store_point.first()
    context['store_point'] = store_point
    context['user'] = staff
    if store_point.store_point.is_main:
        return render(request, 'main_screen/main_screen.html', context)
    else:
        return render(request, 'main_screen/branches_main_screen.html', context)


@login_required(login_url="warehouse_v2:login")
def notification_redirect_view(request, pk):
    staff = request.user

    target_notification = NotificationModel.objects.get(pk=pk)
    if target_notification.receiver == staff:
        target_notification.state = True
        target_notification.save()

        return redirect(target_notification.generated_url)
    else:
        return redirect('warehouse_v2:main_screen')
