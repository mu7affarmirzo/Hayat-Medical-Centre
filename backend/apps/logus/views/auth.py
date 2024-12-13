from datetime import datetime, timedelta

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from apps.account.models import NotificationModel, PatientModel
from apps.decorators import role_required
from apps.logus.forms.booking import BookingForm, PatientRegistrationForm
from apps.logus.forms.registration import DateRangeForm
from apps.logus.models import (
    AvailableRoomsTypeModel, RoomTypeMatrix, AvailableRoomModel,
    AvailableTariffModel, TariffRoomTypeMatrixModel
)
from apps.logus.models.booking import BookingHistory
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
        week_day = WEEKDAYS[date.weekday() + 1]
        formatted_dates.append([day, week_day])

    if len(formatted_dates) > 20:
        formatted_dates = formatted_dates[:20]

    return formatted_dates


@role_required(role='logus', login_url='logus_auth:logout')
def main_screen_view(request):
    context = {}
    staff = request.user

    today = datetime.today()

    tariffs = AvailableTariffModel.objects.all()
    room_types = AvailableRoomsTypeModel.objects.all()

    next_14_days = [today + timedelta(days=i) for i in range(14)]
    formatted_dates = []
    for date in next_14_days:
        day = date.strftime("%d-%B")
        week_day = WEEKDAYS[date.weekday() + 1]
        formatted_dates.append([day, week_day])

    context = {
        'user': staff,
        'days': formatted_dates,
        'tariffs': tariffs,
        'room_types': room_types,
        'selected_room_type': None,
        'selected_start_date': None,
        'selected_end_date': None,
    }

    if request.method == 'POST':
        form = DateRangeForm(request.POST)

        date_range = form.data.get('reservation_time')

        room_type = form.data.get('room_type')
        start_str, end_str = date_range.split(' - ')

        start_date = datetime.strptime(start_str, '%m/%d/%Y')
        end_date = datetime.strptime(end_str, '%m/%d/%Y')

        available_rooms = get_available_rooms(start_date, end_date, room_type)

        formatted_dates = get_the_days_list(start_str, end_str)
        context['days'] = formatted_dates
        context['rooms'] = available_rooms
        context['selected_room_type'] = room_type
        context['selected_date_range'] = date_range

        return render(request, 'logus/main_screen.html', context)

    return render(request, 'logus/main_screen.html', context)


@role_required(role='logus', login_url='logus_auth:logout')
def available_room_view(request):
    context = {}
    staff = request.user

    today = datetime.today()

    tariffs = AvailableTariffModel.objects.all()
    room_types = AvailableRoomsTypeModel.objects.all()

    # Create a matrix dictionary to store the room type and tariff values
    matrix = {}
    for room_type in room_types:
        matrix[room_type] = []
        for tariff in tariffs:
            try:
                value = TariffRoomTypeMatrixModel.objects.get(tariff=tariff, room_type=room_type).price
            except:
                value = None
            matrix[room_type].append(value)

    next_14_days = [today + timedelta(days=i) for i in range(14)]
    formatted_dates = []
    for date in next_14_days:
        day = date.strftime("%d-%B")
        week_day = WEEKDAYS[date.weekday() + 1]
        formatted_dates.append([day, week_day])

    context = {
        'user': staff,
        'days': formatted_dates,
        'tariffs': tariffs,
        'room_types': room_types,
        'matrix': matrix
    }

    if request.method == 'POST':
        form = DateRangeForm(request.POST)

        date_range = form.data.get('reservation_time')

        room_type = form.data.get('room_type')
        start_str, end_str = date_range.split(' - ')

        start_date = datetime.strptime(start_str, '%m/%d/%Y')
        end_date = datetime.strptime(end_str, '%m/%d/%Y')

        available_rooms = get_available_rooms(start_date, end_date, room_type)

        formatted_dates = get_the_days_list(start_str, end_str)
        context['days'] = formatted_dates
        context['rooms'] = available_rooms

        return render(request, 'logus/available_rooms.html', context)

    return render(request, 'logus/available_rooms.html', context)


@role_required(role='logus', login_url='logus_auth:logout')
def register_booking_view(request):

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            illness_history = booking.illness_history.first()
            is_sick_leave = form.cleaned_data.get('is_sick_leave', False)
            return redirect('logus_auth:main_screen')
    else:
        form = BookingForm()
    patients = PatientModel.objects.all()
    rooms = AvailableRoomModel.objects.all()
    room_types = AvailableRoomsTypeModel.objects.all()
    tariffs = AvailableTariffModel.objects.all()
    return render(
        request, 'logus/create_booking.html',
        {
            'form': form,
            'patients': patients,
            'rooms': rooms,
            'room_types': room_types,
            'tariffs': tariffs
        }
    )


@csrf_exempt
def add_new_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.created_by = request.user
            patient.modified_by = request.user
            patient.save()
            return redirect('logus_registration:register-booking')  # Replace with your success URL
    else:
        return redirect('logus_registration:register-booking')
    return render(request, 'logus/create_booking.html', {'form': form})


@role_required(role='logus', login_url='logus_auth:logout')
def notification_redirect_view(request, pk):
    staff = request.user

    target_notification = NotificationModel.objects.get(pk=pk)
    if target_notification.receiver == staff:
        target_notification.state = True
        target_notification.save()

        return redirect(target_notification.generated_url)
    else:
        return redirect('logus_auth:main_screen')


def get_available_rooms(start_date, end_date, room_type):
    rooms_with_matching_type = RoomTypeMatrix.objects.filter(
        room_type__id=int(room_type)
    ).values_list('room_id', flat=True).distinct()

    bookings = BookingHistory.objects.filter(
        Q(start_date__lt=end_date) & Q(end_date__gt=start_date),
        room_id__in=rooms_with_matching_type
    )

    booked_room = {}
    for booking in bookings:
        if booking.room_id in rooms_with_matching_type:
            if booking.room_id not in booked_room:
                booked_room[booking.room_id] = 1
            else:
                booked_room[booking.room_id] += 1

    really_available_rooms = []
    for i in rooms_with_matching_type:
        target_room = AvailableRoomModel.objects.get(id=i)
        if i in booked_room and booked_room[i] > target_room.capacity:
            continue
        else:
            really_available_rooms.append(target_room)
    return really_available_rooms


@role_required(role='logus', login_url='logus_auth:logout')
def test_view(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        print(room_id)
    return HttpResponse('HI')