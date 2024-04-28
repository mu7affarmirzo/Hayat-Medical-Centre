from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.v1.sanatorium.serializers.appointments import RepeatedAppointmentSerializer, FinalAppointmentSerializer, \
    FinalAppointmentDetailedSerializer, ConsultingWithNeurologistSerializer, ConsultingWithCardiologistSerializer, \
    AppointmentWithOnDutyDoctorSerializer, AppointmentWithOnDutyDoctorOnArrivalSerializer, EkgAppointmentSerializer, \
    BasePillsInjectionsModelDetailSerializer, BaseLabResearchServiceModelDetailSerializer, \
    BaseProceduresServicesDetailSerializer, BaseMedicalServicesDetailSerializer
from apps.sanatorium.models import RepeatedAppointmentWithDoctorModel, FinalAppointmentWithDoctorModel, \
    ConsultingWithNeurologistModel, ConsultingWithCardiologistModel, AppointmentWithOnDutyDoctorModel, \
    AppointmentWithOnDutyDoctorOnArrivalModel, EkgAppointmentModel, IllnessHistory, BaseMedicalServiceModel, \
    BaseProcedureServiceModel, BaseLabResearchServiceModel, BasePillsInjectionsModel


def repeated_appointment_post_service(request, pk=None):
    doctor = request.user
    rep_app = RepeatedAppointmentWithDoctorModel(doctor=doctor, created_by=doctor)

    if request.method == "POST":
        serializer = RepeatedAppointmentSerializer(rep_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET" and pk:
        rep_app = get_object_or_404(RepeatedAppointmentWithDoctorModel, pk=pk)
        serializer = RepeatedAppointmentSerializer(rep_app)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH" and pk:
        rep_app = get_object_or_404(RepeatedAppointmentWithDoctorModel, pk=pk)
        serializer = RepeatedAppointmentSerializer(rep_app, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def final_appointment_post_service(request, pk=None):
    doctor = request.user
    rep_app = FinalAppointmentWithDoctorModel(doctor=doctor, created_by=doctor)

    if request.method == "POST":
        serializer = FinalAppointmentSerializer(rep_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = FinalAppointmentDetailedSerializer(rep_app)
            return Response(response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET" and pk:
        rep_app = get_object_or_404(FinalAppointmentWithDoctorModel, pk=pk)
        serializer = FinalAppointmentSerializer(rep_app)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH" and pk:
        rep_app = get_object_or_404(FinalAppointmentWithDoctorModel, pk=pk)
        serializer = FinalAppointmentSerializer(rep_app, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def consulting_with_neurologist_post_service(request, pk=None):
    doctor = request.user
    rep_app = ConsultingWithNeurologistModel(doctor=doctor, created_by=doctor)

    if request.method == "POST":
        serializer = ConsultingWithNeurologistSerializer(rep_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET" and pk:
        rep_app = get_object_or_404(ConsultingWithNeurologistModel, pk=pk)
        serializer = ConsultingWithNeurologistSerializer(rep_app)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH" and pk:
        rep_app = get_object_or_404(ConsultingWithNeurologistModel, pk=pk)
        serializer = ConsultingWithNeurologistSerializer(rep_app, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def consulting_with_cardiologist_post_service(request, pk=None):
    doctor = request.user
    rep_app = ConsultingWithCardiologistModel(doctor=doctor, created_by=doctor)

    if request.method == "POST":
        serializer = ConsultingWithCardiologistSerializer(rep_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET" and pk:
        rep_app = get_object_or_404(ConsultingWithCardiologistModel, pk=pk)
        serializer = ConsultingWithCardiologistSerializer(rep_app)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH" and pk:
        rep_app = get_object_or_404(ConsultingWithCardiologistModel, pk=pk)
        serializer = ConsultingWithCardiologistSerializer(rep_app, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def appointment_with_on_duty_doctor_post_service(request, pk=None):
    doctor = request.user
    rep_app = AppointmentWithOnDutyDoctorModel(doctor=doctor, created_by=doctor)

    if request.method == "POST":
        serializer = AppointmentWithOnDutyDoctorSerializer(rep_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET" and pk:
        rep_app = get_object_or_404(AppointmentWithOnDutyDoctorModel, pk=pk)
        serializer = AppointmentWithOnDutyDoctorSerializer(rep_app)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH" and pk:
        rep_app = get_object_or_404(AppointmentWithOnDutyDoctorModel, pk=pk)
        serializer = AppointmentWithOnDutyDoctorSerializer(rep_app, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def appointment_with_on_duty_doctor_on_arrival_service(request, pk=None):
    doctor = request.user
    rep_app = AppointmentWithOnDutyDoctorOnArrivalModel(doctor=doctor, created_by=doctor)

    if request.method == "POST":
        serializer = AppointmentWithOnDutyDoctorOnArrivalSerializer(rep_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET" and pk:
        rep_app = get_object_or_404(AppointmentWithOnDutyDoctorOnArrivalModel, pk=pk)
        serializer = AppointmentWithOnDutyDoctorOnArrivalSerializer(rep_app)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH" and pk:
        rep_app = get_object_or_404(AppointmentWithOnDutyDoctorOnArrivalModel, pk=pk)
        serializer = AppointmentWithOnDutyDoctorOnArrivalSerializer(rep_app, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def ekg_appointment_service(request, pk=None):
    doctor = request.user
    app = EkgAppointmentModel(doctor=doctor, created_by=doctor)

    if request.method == "POST":
        serializer = EkgAppointmentSerializer(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET" and pk:
        rep_app = get_object_or_404(EkgAppointmentModel, pk=pk)
        serializer = EkgAppointmentSerializer(rep_app)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH" and pk:
        rep_app = get_object_or_404(EkgAppointmentModel, pk=pk)
        serializer = EkgAppointmentSerializer(rep_app, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def get_list_of_appointments_service(request, pk):
    ill_history = get_object_or_404(IllnessHistory, pk=pk)
    med_services = BaseMedicalServiceModel.objects.filter(illness_history=ill_history)
    procedures_services = BaseProcedureServiceModel.objects.filter(illness_history=ill_history)
    labs = BaseLabResearchServiceModel.objects.filter(illness_history=ill_history)
    pill_injections = BasePillsInjectionsModel.objects.filter(illness_history=ill_history)

    med_services_serializer = BaseMedicalServicesDetailSerializer(med_services, many=True)
    procedures_services_serializer = BaseProceduresServicesDetailSerializer(procedures_services, many=True)
    labs_serializer = BaseLabResearchServiceModelDetailSerializer(labs, many=True)
    pill_injections_serializer = BasePillsInjectionsModelDetailSerializer(pill_injections, many=True)

    return Response({
        'med_services': med_services_serializer.data,
        'procedures_services': procedures_services_serializer.data,
        'labs': labs_serializer.data,
        'pill_injections': pill_injections_serializer.data,
    })

