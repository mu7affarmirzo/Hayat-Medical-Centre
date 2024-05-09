from rest_framework.generics import get_object_or_404

from apps.sanatorium.models import (
    ArterialPressureModel,
    GlucometerModel,
    PulseModel,
    SaturationModel,
    TemperatureModel
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
    # elif request.method == "GET" and pk:
    #     rep_measurement = get_object_or_404(EkgmeasurementointmentModel, pk=pk)
    #     serializer = GetEkgmeasurementointmentSerializer(rep_measurement)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # elif request.method == "PATCH" and pk:
    #     rep_measurement = get_object_or_404(EkgmeasurementointmentModel, pk=pk)
    #     serializer = EkgmeasurementointmentSerializer(rep_measurement, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def measured_params_glucometer_service(request, pk=None):
    doctor = request.user
    measurement = GlucometerModel(created_by=doctor)

    if request.method == "POST":
        serializer = GlucometerSerializer(measurement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == "GET" and pk:
    #     rep_measurement = get_object_or_404(EkgmeasurementointmentModel, pk=pk)
    #     serializer = GetEkgmeasurementointmentSerializer(rep_measurement)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # elif request.method == "PATCH" and pk:
    #     rep_measurement = get_object_or_404(EkgmeasurementointmentModel, pk=pk)
    #     serializer = EkgmeasurementointmentSerializer(rep_measurement, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
    # elif request.method == "GET" and pk:
    #     rep_measurement = get_object_or_404(EkgmeasurementointmentModel, pk=pk)
    #     serializer = GetEkgmeasurementointmentSerializer(rep_measurement)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # elif request.method == "PATCH" and pk:
    #     rep_measurement = get_object_or_404(EkgmeasurementointmentModel, pk=pk)
    #     serializer = EkgmeasurementointmentSerializer(rep_measurement, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
    # elif request.method == "GET" and pk:
    #     rep_measurement = get_object_or_404(EkgmeasurementointmentModel, pk=pk)
    #     serializer = GetEkgmeasurementointmentSerializer(rep_measurement)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # elif request.method == "PATCH" and pk:
    #     rep_measurement = get_object_or_404(EkgmeasurementointmentModel, pk=pk)
    #     serializer = EkgmeasurementointmentSerializer(rep_measurement, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
    # elif request.method == "GET" and pk:
    #     rep_measurement = get_object_or_404(EkgmeasurementointmentModel, pk=pk)
    #     serializer = GetEkgmeasurementointmentSerializer(rep_measurement)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # elif request.method == "PATCH" and pk:
    #     rep_measurement = get_object_or_404(EkgmeasurementointmentModel, pk=pk)
    #     serializer = EkgmeasurementointmentSerializer(rep_measurement, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

