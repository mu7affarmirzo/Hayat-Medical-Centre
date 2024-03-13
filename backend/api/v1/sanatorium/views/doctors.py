from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.sanatorium.serializers import *
from apps.sanatorium.models import *


@swagger_auto_schema(tags=['sanatorium'], method="get", )
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def ib_by_id_doctors_view(request, pk):
    context = {
        "documents": {},
        "regime": "",
        "highlighted_tags": {
            "allergy": False,
            "meteolabel": False,
            "food_issues": False,
            "furniture_fault": False,
            "pills_drugs": False
        }
    }
    ill_his = get_object_or_404(IllnessHistory, pk=pk)
    serializer = DoctorsIllnessHistorySerializer(ill_his)

    return Response({**serializer.data, **context})


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=InitialAppointmentWithDoctorSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def init_appointment_with_doctor_view(request):
    doctor = request.user
    init_app = InitialAppointmentWithDoctorModel(doctor=doctor)

    if request.method == "POST":
        serializer = InitialAppointmentWithDoctorSerializer(init_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(tags=['sanatorium'], method="patch", request_body=InitialAppointmentWithDoctorSerializer)
@api_view(['PATCH', ])
@permission_classes((IsAuthenticated,))
def update_init_appointment_with_doctor_view(request, pk):
    initial_obj = get_object_or_404(InitialAppointmentWithDoctorModel, pk=pk)
    serializer = InitialAppointmentWithDoctorSerializer(initial_obj, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(tags=['sanatorium'], method="get")
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def get_init_appointment_view(request, pk):
    """
    pk from illness history
    """
    appointment = get_object_or_404(InitialAppointmentWithDoctorModel, pk=pk)
    serializer = InitialAppointmentWithDoctorSerializer(appointment)
    return Response(serializer)
