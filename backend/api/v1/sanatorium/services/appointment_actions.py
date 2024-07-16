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
    ctx = []
    data_target = request.data

    if request.method == "POST":
        for data in data_target:
            rep_app = BaseMedicalServiceModel(created_by=doctor)
            serializer = CreateBaseMedicalServicesSerializer(rep_app, data=data)

            if serializer.is_valid():
                serializer.save()
                ctx.append(serializer.data)
            else:
                ctx.append(serializer.errors)
    return Response(ctx)


def create_appointments_actions_lab_research_service(request):
    doctor = request.user
    ctx = []
    data_target = request.data

    if request.method == "POST":
        for data in data_target:
            rep_app = BaseLabResearchServiceModel(created_by=doctor)
            serializer = CreateBaseLabResearchServiceSerializer(rep_app, data=data)

            if serializer.is_valid():
                serializer.save()
                ctx.append(serializer.data)
            else:
                ctx.append(serializer.errors)
    return Response(ctx)


def create_appointments_actions_procedures_service(request):
    doctor = request.user
    ctx = []
    data_target = request.data

    if request.method == "POST":
        for data in data_target:
            rep_app = BaseProcedureServiceModel(created_by=doctor)
            serializer = CreateBaseProceduresSerializer(rep_app, data=data)

            if serializer.is_valid():
                serializer.save()
                ctx.append(serializer.data)
            else:
                ctx.append(serializer.errors)
    return Response(ctx)


def create_appointments_actions_pills_service(request):
    doctor = request.user
    ctx = []
    data_target = request.data

    if request.method == "POST":
        for data in data_target:
            rep_app = BasePillsInjectionsModel(created_by=doctor)
            serializer = CreateBasePPillsInjectionsSerializer(rep_app, data=data)
            if serializer.is_valid():
                serializer.save()
                ctx.append(serializer.data)
            else:
                ctx.append(serializer.errors)
    return Response(ctx)

