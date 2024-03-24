from rest_framework import status
from rest_framework.response import Response

from api.v1.sanatorium.serializers.appointments import RepeatedAppointmentSerializer, FinalAppointmentSerializer, \
    FinalAppointmentDetailedSerializer, ConsultingWithNeurologistSerializer
from apps.sanatorium.models import RepeatedAppointmentWithDoctorModel, FinalAppointmentWithDoctorModel, \
    ConsultingWithNeurologistModel


def repeated_appointment_post_service(request):
    doctor = request.user
    rep_app = RepeatedAppointmentWithDoctorModel(doctor=doctor, created_by=doctor)

    if request.method == "POST":
        serializer = RepeatedAppointmentSerializer(rep_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def final_appointment_post_service(request):
    doctor = request.user
    rep_app = FinalAppointmentWithDoctorModel(doctor=doctor, created_by=doctor)

    if request.method == "POST":
        serializer = FinalAppointmentSerializer(rep_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = FinalAppointmentDetailedSerializer(rep_app)
            return Response(response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def consulting_with_neurologist_post_service(request):
    doctor = request.user
    rep_app = ConsultingWithNeurologistModel(doctor=doctor, created_by=doctor)

    if request.method == "POST":
        serializer = ConsultingWithNeurologistSerializer(rep_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # response = FinalAppointmentDetailedSerializer(rep_app)
            # return Response(response.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
