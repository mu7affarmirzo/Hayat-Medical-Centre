from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from api.v1.sanatorium.serializers import BaseMedicalServicesSerializer, BaseLabResearchServiceSerializer, \
    BaseProceduresSerializer, BasePPillsInjectionsSerializer
from api.v1.sanatorium.serializers.appointments import CreateBasePPillsInjectionsSerializer, \
    CreateBaseLabResearchServiceSerializer, CreateBaseProceduresSerializer, CreateBaseMedicalServicesSerializer
from apps.sanatorium.models import IllnessHistory, BaseMedicalServiceModel, BaseLabResearchServiceModel, \
    BaseProcedureServiceModel, BasePillsInjectionsModel


def get_list_of_appointments_actions_service(request, pk):
    ill_history = get_object_or_404(IllnessHistory, pk=pk)

    medical_services = BaseMedicalServiceModel.objects.filter(illness_history=ill_history)
    lab_research = BaseLabResearchServiceModel.objects.filter(illness_history=ill_history)
    procedures = BaseProcedureServiceModel.objects.filter(illness_history=ill_history)
    pills = BasePillsInjectionsModel.objects.filter(illness_history=ill_history)

    medical_services = BaseMedicalServicesSerializer(medical_services, many=True)
    lab_research = BaseLabResearchServiceSerializer(lab_research, many=True)
    procedures = BaseProceduresSerializer(procedures, many=True)
    pills = BasePPillsInjectionsSerializer(pills, many=True)

    return Response({
        "medical_services": medical_services.data,
        "lab_research": lab_research.data,
        "procedures": procedures.data,
        "pills": pills.data,
    })


def create_appointments_actions_medical_services_service(request):
    doctor = request.user
    rep_app = BaseMedicalServiceModel(created_by=doctor)

    if request.method == "POST":
        serializer = CreateBaseMedicalServicesSerializer(rep_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create_appointments_actions_lab_research_service(request):
    doctor = request.user
    rep_app = BaseProcedureServiceModel(created_by=doctor)

    if request.method == "POST":
        serializer = CreateBaseProceduresSerializer(rep_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create_appointments_actions_procedures_service(request):
    doctor = request.user
    rep_app = BaseLabResearchServiceModel(created_by=doctor)

    if request.method == "POST":
        serializer = CreateBaseLabResearchServiceSerializer(rep_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create_appointments_actions_pills_service(request):
    doctor = request.user
    rep_app = BasePillsInjectionsModel(created_by=doctor)

    if request.method == "POST":
        serializer = CreateBasePPillsInjectionsSerializer(rep_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

