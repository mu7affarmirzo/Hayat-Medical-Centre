from rest_framework.generics import get_object_or_404

from apps.sanatorium.models import (
    ArterialPressureModel,
    GlucometerModel,
    PulseModel,
    SaturationModel,
    TemperatureModel, IllnessHistory
)

from rest_framework import status
from rest_framework.response import Response

from api.v1.sanatorium.serializers.measured_params import (
    ArterialPressureSerializer,
    GlucometerSerializer,
    PulseSerializer,
    SaturationSerializer,
    TemperatureSerializer
)


def measured_params_arterial_service(request, pk=None):
    doctor = request.user
    measurement = ArterialPressureModel(created_by=doctor)

    if request.method == "POST":
        serializer = ArterialPressureSerializer(measurement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET" and pk:
        rep_measurement = get_object_or_404(ArterialPressureModel, pk=pk)
        serializer = ArterialPressureSerializer(rep_measurement)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH" and pk:
        rep_measurement = get_object_or_404(ArterialPressureModel, pk=pk)
        serializer = ArterialPressureSerializer(rep_measurement, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def list_measured_params_arterial_service(request, pk):
    ill_hist = get_object_or_404(IllnessHistory, pk=pk)
    arterial = ill_hist.arterial_pressure.all()
    serializer = ArterialPressureSerializer(arterial, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def measured_params_glucometer_service(request, pk=None):
    doctor = request.user
    measurement = GlucometerModel(created_by=doctor)

    if request.method == "POST":
        serializer = GlucometerSerializer(measurement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET" and pk:
        rep_measurement = get_object_or_404(GlucometerModel, pk=pk)
        serializer = GlucometerSerializer(rep_measurement)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH" and pk:
        rep_measurement = get_object_or_404(GlucometerModel, pk=pk)
        serializer = GlucometerSerializer(rep_measurement, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def measured_params_pulse_service(request, pk=None):
    doctor = request.user
    measurement = PulseModel(created_by=doctor)

    if request.method == "POST":
        serializer = PulseSerializer(measurement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET" and pk:
        rep_measurement = get_object_or_404(PulseModel, pk=pk)
        serializer = PulseSerializer(rep_measurement)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH" and pk:
        rep_measurement = get_object_or_404(PulseModel, pk=pk)
        serializer = PulseSerializer(rep_measurement, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def measured_params_saturation_service(request, pk=None):
    doctor = request.user
    measurement = SaturationModel(created_by=doctor)

    if request.method == "POST":
        serializer = SaturationSerializer(measurement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET" and pk:
        rep_measurement = get_object_or_404(SaturationModel, pk=pk)
        serializer = SaturationSerializer(rep_measurement)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH" and pk:
        rep_measurement = get_object_or_404(SaturationModel, pk=pk)
        serializer = SaturationSerializer(rep_measurement, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def measured_params_temperature_service(request, pk=None):
    doctor = request.user
    measurement = TemperatureModel(created_by=doctor)

    if request.method == "POST":
        serializer = TemperatureSerializer(measurement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET" and pk:
        rep_measurement = get_object_or_404(TemperatureModel, pk=pk)
        serializer = TemperatureSerializer(rep_measurement)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH" and pk:
        rep_measurement = get_object_or_404(TemperatureModel, pk=pk)
        serializer = TemperatureSerializer(rep_measurement, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

