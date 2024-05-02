from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from api.v1.sanatorium.serializers.appointments import (RepeatedAppointmentSerializer, FinalAppointmentSerializer, \
                                                        ConsultingWithNeurologistSerializer,
                                                        ConsultingWithCardiologistSerializer,
                                                        AppointmentWithOnDutyDoctorSerializer,
                                                        AppointmentWithOnDutyDoctorOnArrivalModel,
                                                        AppointmentWithOnDutyDoctorOnArrivalSerializer,
                                                        EkgAppointmentSerializer)
from api.v1.sanatorium.services.appointments import (
    repeated_appointment_post_service, final_appointment_post_service,
    consulting_with_neurologist_post_service, consulting_with_cardiologist_post_service,
    appointment_with_on_duty_doctor_post_service, appointment_with_on_duty_doctor_on_arrival_service,
    ekg_appointment_service, get_list_of_appointments_service, get_list_of_appointments_sheet_service
)


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=RepeatedAppointmentSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def repeated_appointment_with_doctor_view(request):
    return repeated_appointment_post_service(request)


@swagger_auto_schema(tags=['sanatorium'], methods=["patch", "get"])
@api_view(['PATCH', 'GET'])
@permission_classes((IsAuthenticated,))
def get_update_repeated_appointment_with_doctor_view(request, pk):
    return repeated_appointment_post_service(request, pk)


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=FinalAppointmentSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def final_appointment_with_doctor_view(request):
    return final_appointment_post_service(request)


@swagger_auto_schema(tags=['sanatorium'], methods=["patch", "get"])
@api_view(['PATCH', 'GET'])
@permission_classes((IsAuthenticated,))
def get_update_final_appointment_with_doctor_view(request, pk):
    return final_appointment_post_service(request, pk)


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=ConsultingWithNeurologistSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def consulting_with_neurologist_view(request):
    return consulting_with_neurologist_post_service(request)


@swagger_auto_schema(tags=['sanatorium'], methods=["patch", "get"])
@api_view(['PATCH', 'GET'])
@permission_classes((IsAuthenticated,))
def get_update_consulting_with_neurologist_view(request, pk):
    return consulting_with_neurologist_post_service(request, pk)


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=ConsultingWithCardiologistSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def consulting_with_cardiologist_view(request):
    return consulting_with_cardiologist_post_service(request)


@swagger_auto_schema(tags=['sanatorium'], methods=["patch", "get"])
@api_view(['PATCH', 'GET'])
@permission_classes((IsAuthenticated,))
def get_update_consulting_with_cardiologist_view(request, pk):
    return consulting_with_cardiologist_post_service(request, pk)


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=AppointmentWithOnDutyDoctorSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def appointment_with_on_duty_doctor_view(request):
    return appointment_with_on_duty_doctor_post_service(request)


@swagger_auto_schema(tags=['sanatorium'], methods=["patch", "get"])
@api_view(['PATCH', 'GET'])
@permission_classes((IsAuthenticated,))
def get_update_appointment_with_on_duty_doctor_view(request, pk):
    return appointment_with_on_duty_doctor_post_service(request, pk)


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=AppointmentWithOnDutyDoctorOnArrivalSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def appointment_with_on_duty_doctor_on_arrival_view(request):
    return appointment_with_on_duty_doctor_on_arrival_service(request)


@swagger_auto_schema(tags=['sanatorium'], methods=["patch", "get"])
@api_view(['PATCH', 'GET'])
@permission_classes((IsAuthenticated,))
def get_update_appointment_with_on_duty_doctor_on_arrival_view(request, pk):
    return appointment_with_on_duty_doctor_on_arrival_service(request, pk)


@swagger_auto_schema(tags=['sanatorium'], method="post", request_body=EkgAppointmentSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def ekg_appointment_view(request):
    return ekg_appointment_service(request)


@swagger_auto_schema(tags=['sanatorium'], methods=["patch", "get"])
@api_view(['PATCH', 'GET'])
@permission_classes((IsAuthenticated,))
def get_update_ekg_appointment_view(request, pk):
    return ekg_appointment_service(request, pk)


@swagger_auto_schema(tags=['sanatorium'], method="get")
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_list_of_appointments_sheet_view(request, pk):
    return get_list_of_appointments_sheet_service(request, pk)


@swagger_auto_schema(tags=['sanatorium'], method="get")
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_list_of_appointments_view(request, pk):
    return get_list_of_appointments_service(request, pk)
