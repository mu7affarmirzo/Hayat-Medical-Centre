import locale

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.account.models import NotificationModel
from apps.logus.forms.registration import DateRangeForm
from apps.warehouse.forms import AccountAuthenticationForm
from apps.warehouse.models.store_point import StorePointStaffModel

from datetime import datetime, timedelta


# locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

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
        return redirect("logus_auth:main_screen")


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("logus_auth:main_screen")
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("logus_auth:main_screen")

    form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'auth/login.html', context)


@login_required(login_url="logus_auth:login")
def logout_view(request):
    logout(request)
    return redirect('logus_auth:login')


def get_the_days_list(start_date, end_date):
    start_date = datetime.strptime(start_date, '%m/%d/%Y')
    end_date = datetime.strptime(end_date, '%m/%d/%Y')

    # Create a list of days between start_date and end_date
    delta = end_date - start_date
    selected_days = [start_date + timedelta(days=i) for i in range(delta.days + 1)]

    # Format the dates to include the day of the week and the specified format in Russian
    formatted_dates = []
    for date in selected_days:
        day = date.strftime("%d-%B")
        week_day = WEEKDAYS[date.weekday()+1]
        formatted_dates.append([day, week_day])

    if len(formatted_dates) > 20:
        formatted_dates = formatted_dates[:20]

    return formatted_dates


@login_required(login_url="logus_auth:login")
def main_screen_view(request):
    context = {}
    staff = request.user

    today = datetime.today()

    next_14_days = [today + timedelta(days=i) for i in range(14)]
    formatted_dates = []
    for date in next_14_days:
        day = date.strftime("%d-%B")
        week_day = WEEKDAYS[date.weekday()+1]
        formatted_dates.append([day, week_day])

    if request.method == 'POST':
        data = DateRangeForm(request.POST)
        date_range = data.data.get('reservation_time')
        start_str, end_str = date_range.split(' - ')

        formatted_dates = get_the_days_list(start_str, end_str)

        context['user'] = staff
        context['days'] = formatted_dates

        return render(request, 'logus/main_screen.html', context)

    context['user'] = staff
    context['days'] = formatted_dates

    return render(request, 'logus/main_screen.html', context)


@login_required(login_url="logus_auth:login")
def notification_redirect_view(request, pk):
    staff = request.user

    target_notification = NotificationModel.objects.get(pk=pk)
    if target_notification.receiver == staff:
        target_notification.state = True
        target_notification.save()

        return redirect(target_notification.generated_url)
    else:
        return redirect('logus_auth:main_screen')
