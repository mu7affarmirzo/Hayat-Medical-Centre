from apps.account.models import PatientModel
from apps.logus.models import BookedRoomModel

# Create your views here.

from django.shortcuts import render, HttpResponse
import datetime


# def search(requests):
#     a = datetime.datetime.today()
#
#     if requests.method == "POST":
#         data = requests.POST['inputValue']
#
#         p = PatientModel.objects.filter(Q(f_name=data) | Q(l_name=data) | Q(mid_name=data)).first()
#
#         room_model = BookedRoomModel.objects.filter(patients=p)
#         print(room_model)
#         return render(requests, 'Hospital/patients-my-patients.html',
#                       {"room": room_model, "room_len": len(room_model), "today": a.year})
#
#     room = BookedRoomModel.objects.all().order_by('id')
#     ctx = {
#         "today": a.year,
#         "room": room,
#         "room_len": len(room),
#     }
#     return render(requests, 'Hospital/patients-my-patients.html', ctx)
#

def patients_m_p(requests):
    a = datetime.datetime.today()
    room = BookedRoomModel.objects.all().order_by('id')
    ctx = {
        "today": a.year,
        "room": room,
        "room_len": len(room),
    }
    return render(requests, 'Hospital/patients-my-patients.html', ctx)


def dispatching_m_p(requests):
    return render(requests, 'Hospital/dispatching-my-patients.html', {})


def dispatching_p_g(requests):
    return render(requests, 'Hospital/dispatching-patient-gidrokolonoterapiya.html', {})


def dispatching_p_h(requests):
    return render(requests, 'Hospital/dispatching-patient-hydrobaths.html', {})


def dispatching_p_i(requests):
    return render(requests, 'Hospital/dispatching-patient-info.html', {})


def dispatching_p_s(requests):
    return render(requests, 'Hospital/dispatching-patient-schedule.html', {})


def events(requests):
    return render(requests, 'Hospital/events.html', {})


def login(requests):
    return render(requests, 'Hospital/login.html', {})


def patients_a(requests):
    return render(requests, 'Hospital/patients-accounts.html', {})


def patients_s(requests):
    return render(requests, 'Hospital/patients-search.html', {})


def register(requests):
    return render(requests, 'Hospital/register.html', {})


def register_a_sh(requests):
    return render(requests, 'Hospital/register-appointment_sheet.html', {})


def register_ch(requests):
    return render(requests, 'Hospital/register-changelog.html', {})


def register_c(requests):
    return render(requests, 'Hospital/register-count.html', {})


def register_d(requests):
    return render(requests, 'Hospital/register-document.html', {})


def register_m_h(requests):
    return render(requests, 'Hospital/register-medical-history.html', {})


def register_o(requests):
    return render(requests, 'Hospital/register-outpatient.html', {})


def register_p(requests):
    return render(requests, 'Hospital/register-patient.html', {})


def register_p_s(requests):
    return render(requests, 'Hospital/register-patient-step-1.html', {})


def register_s(requests):
    return render(requests, 'Hospital/register-schedule.html', {})
