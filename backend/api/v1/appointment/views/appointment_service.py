import random

from apps.account.models import AppointmentServiceModel, MedicalService, DoctorAccountModel
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from api.v1.appointment.serializers.appointment import AppointmentServiceSerializers, \
    AppointmentServiceCreateSerializers, MedicalServiceSerializers


@swagger_auto_schema(method="get", tags=["appointment-service"])
@api_view(['GET', ])
def setup_service(request):
    med_services = MedicalService.objects.all()
    doctors = DoctorAccountModel.objects.all()
    print(doctors.values())
    for serv in med_services:
        print(random.choice(doctors))
        serv.doctor.add(random.choice(doctors))
        serv.save()
    serializer = MedicalServiceSerializers(med_services, many=True)
    return Response(serializer.data)


class AppointmentServiceView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['appointment-service'])
    def get(self, requset, format=None):
        apps = AppointmentServiceModel.objects.all()
        serializer = AppointmentServiceSerializers(apps, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['appointment-service'], request_body=AppointmentServiceCreateSerializers)
    def post(self, request, format=None):
        account = request.user
        app = AppointmentServiceModel(created_by=account, modified_by=account)
        serializer = AppointmentServiceCreateSerializers(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentServiceRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AppointmentServiceSerializers

    def get_queryset(self, ):
        return AppointmentServiceModel.objects.all()

    @swagger_auto_schema(tags=['appointment-service'])
    def get(self, request, pk, format=None):
        try:
            app = AppointmentServiceModel.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AppointmentServiceSerializers(app)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['appointment-service'], request_body=AppointmentServiceCreateSerializers)
    def put(self, request, pk, format=None):
        try:
            app = AppointmentServiceModel.objects.get(pk=pk)
            app.modified_by = request.user
            app.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentServiceCreateSerializers(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['appointment-service'])
    def delete(self, request, pk, format=None):
        try:
            app = AppointmentServiceModel.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        app.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
