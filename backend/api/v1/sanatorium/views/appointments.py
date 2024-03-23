from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.sanatorium.serializers import *
from api.v1.sanatorium.serializers.appointments import RepeatedAppointmentSerializer
from api.v1.sanatorium.services.appointments import repeated_appointment_post_service
from apps.account.models import SpecialityModel
from apps.sanatorium.models import *


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=RepeatedAppointmentSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def repeated_appointment_with_doctor_view(request):
    return repeated_appointment_post_service(request)
