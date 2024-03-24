from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from api.v1.sanatorium.serializers.appointments import RepeatedAppointmentSerializer, FinalAppointmentSerializer
from api.v1.sanatorium.services.appointments import repeated_appointment_post_service, final_appointment_post_service


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=RepeatedAppointmentSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def repeated_appointment_with_doctor_view(request):
    return repeated_appointment_post_service(request)


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=FinalAppointmentSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def final_appointment_with_doctor_view(request):
    return final_appointment_post_service(request)
