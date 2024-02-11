from django.db.models import Q, Count

from api.v1.sanatorium.serializers import *
from apps.sanatorium.models import *


def get_patients(request):
    user = request.user
    patients_response = []
    patients = IllnessHistory.objects.filter(doctor=user)
    for patient in patients:
        patients_response.append({
            "cito": None, "no": patient.series_number, "age": patient.patient.age,
            "room": patient.booking.room.room_number, "dispatch": patient.diagnosis.name,
            "start_date": patient.booking.start_date, "end_date": patient.booking.end_date,
            "doctor": patient.doctor.full_name, "name": patient.patient.full_name
        })
    return patients_response


def get_patients(request):
    user = request.user

    # query_params
    names = request.query_params.get('full_name')
    first_name = names[0]
    last_name = names[-1]
    mid_name = names[1] if len(names) > 2 else None

    ib = request.query_params.get('ib')
    card_type = request.query_params.get('full_name')
    word = request.query_params.get('word')

    patients_response = []
    patients = IllnessHistory.objects.filter(doctor=user).filter(
        Q(patient__f_name__icontains=first_name) |
        Q(patient__l_name__icontains=last_name) |
        Q(patient__mid_name__icontains=mid_name) |
        Q(series_number=ib))
    for patient in patients:
        patients_response.append({
            "cito": None, "no": patient.series_number, "age": patient.patient.age,
            "room": patient.booking.room.room_number, "dispatch": ["", ""],
            "start_date": patient.booking.start_date, "end_date": patient.booking.end_date,
            "doctor": patient.doctor.full_name, "name": patient.patient.full_name
        })
    return patients_response