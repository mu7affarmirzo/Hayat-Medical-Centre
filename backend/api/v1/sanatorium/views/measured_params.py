from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from api.v1.sanatorium.serializers.measured_params import (
    ArterialPressureSerializer,
    GlucometerSerializer,
    PulseSerializer,
    SaturationSerializer,
    TemperatureSerializer,
)
from api.v1.sanatorium.services.measured_params import (
    measured_params_temperature_service, measured_params_saturation_service,
    measured_params_pulse_service, measured_params_arterial_service,
    measured_params_glucometer_service
)


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=ArterialPressureSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def measured_params_arterial_view(request):
    return measured_params_arterial_service(request)


@swagger_auto_schema(tags=['sanatorium'], methods=["patch", "get"])
@api_view(['PATCH', 'GET'])
@permission_classes((IsAuthenticated,))
def measured_params_arterial_view(request, pk):
    return measured_params_arterial_service(request, pk)


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=GlucometerSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def measured_params_glucometer_view(request):
    return measured_params_glucometer_service(request)


@swagger_auto_schema(tags=['sanatorium'], methods=["patch", "get"])
@api_view(['PATCH', 'GET'])
@permission_classes((IsAuthenticated,))
def measured_params_glucometer_view(request, pk):
    return measured_params_glucometer_service(request, pk)


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=PulseSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def measured_params_pulse_view(request):
    return measured_params_pulse_service(request)


@swagger_auto_schema(tags=['sanatorium'], methods=["patch", "get"])
@api_view(['PATCH', 'GET'])
@permission_classes((IsAuthenticated,))
def measured_params_pulse_view(request, pk):
    return measured_params_pulse_service(request, pk)


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=SaturationSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def measured_params_saturation_view(request):
    return measured_params_saturation_service(request)


@swagger_auto_schema(tags=['sanatorium'], methods=["patch", "get"])
@api_view(['PATCH', 'GET'])
@permission_classes((IsAuthenticated,))
def measured_params_saturation_view(request, pk):
    return measured_params_saturation_service(request, pk)


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=TemperatureSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def measured_params_temperature_view(request):
    return measured_params_temperature_service(request)


@swagger_auto_schema(tags=['sanatorium'], methods=["patch", "get"])
@api_view(['PATCH', 'GET'])
@permission_classes((IsAuthenticated,))
def measured_params_temperature_view(request, pk):
    return measured_params_temperature_service(request, pk)

