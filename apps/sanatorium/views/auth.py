from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.account.models import NotificationModel, PatientModel, AccountRolesModel
from apps.decorators import role_required

from apps.warehouse.forms import AccountAuthenticationForm
from apps.warehouse.models.store_point import StorePointStaffModel


WEEKDAYS = {
    1: 'Пн',
    2: 'Вт',
    3: 'Ср',
    4: 'Чт',
    5: 'Пт',
    6: 'Сб',
    7: 'Вс',
}


def user_redirect(user):
    role_page = StorePointStaffModel.objects.filter(staff__in=[user]).first()
    if role_page:
        return redirect(role_page.role.name)
    else:
        return redirect("sanatorium_auth:main_screen")


def login_view(request):
    context = {}
    user = request.user

    if user.is_authenticated:
        return redirect("sanatorium_auth:main_screen")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():

            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("sanatorium_auth:main_screen")

    form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'sanatorium/sanatorium_auth/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


@role_required(role='sanatorium', login_url='sanatorium_auth:logout')
def main_screen_view(request):

    target_role = AccountRolesModel.objects.filter(user=request.user)
    target_role = target_role.first()
    if target_role:
        target_role = target_role.role.name

    user_role_based_redirect = {
        'warehouse': 'warehouse_v2:main_screen',
        'sanatorium.staff': 'sanatorium_staff:main_screen',
        'sanatorium.nurse': 'sanatorium_nurse:main_screen',
        'sanatorium.admin': 'sanatorium_admin:main_screen',
        'sanatorium.doctor': 'sanatorium_doctors:main_screen',
    }

    if target_role in user_role_based_redirect:
        print(user_role_based_redirect[target_role])
        return redirect(user_role_based_redirect[target_role])
    return redirect('sanatorium_auth:logout')


@role_required(role='sanatorium', login_url='sanatorium_auth:logout')
def notification_redirect_view(request, pk):
    staff = request.user

    target_notification = NotificationModel.objects.get(pk=pk)
    if target_notification.receiver == staff:
        target_notification.state = True
        target_notification.save()

        return redirect(target_notification.generated_url)
    else:
        return redirect('sanatorium_auth:main_screen')


