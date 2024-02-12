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
    full_name = request.query_params.get('full_name')
    first_name = None
    last_name = None
    mid_name = None

    if full_name:
        names = full_name.split()
        if len(names) > 1:
            first_name = names[0]
            last_name = names[-1]
            mid_name = names[1] if len(names) > 2 else None
        else:
            first_name = names[0]

    ib = request.query_params.get('ib')
    card_type = request.query_params.get('full_name')
    word = request.query_params.get('word')

    patients_response = []
    patients = IllnessHistory.objects.filter(doctor=user)

    if first_name:
        patients = patients.filter(patient__f_name=first_name)
    if mid_name:
        patients = patients.filter(patient__mid_name=mid_name)
    if last_name:
        patients = patients.filter(patient__l_name=last_name)
    if ib:
        patients = patients.filter(series_number=ib)

    for patient in patients:
        patients_response.append({
            "id": patient.id,
            "cito": None, "no": patient.series_number, "age": patient.patient.age,
            "room": patient.booking.room.room_number, "dispatch": ["", ""],
            "start_date": patient.booking.start_date, "end_date": patient.booking.end_date,
            "doctor": patient.doctor.full_name, "name": patient.patient.full_name
        })
    return patients_response