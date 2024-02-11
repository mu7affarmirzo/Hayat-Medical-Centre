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
    patients_response = []
    patients = IllnessHistory.objects.filter(doctor=user)
    for patient in patients:
        patients_response.append({
            "cito": None, "no": patient.series_number, "age": patient.patient.age,
            "room": patient.booking.room.room_number, "dispatch": ["", ""],
            "start_date": patient.booking.start_date, "end_date": patient.booking.end_date,
            "doctor": patient.doctor.full_name, "name": patient.patient.full_name
        })
    return patients_response