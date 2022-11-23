from apps.account.models import AppointmentsModel, AppointmentServiceModel
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from api.v1.appointment.serializers.appointment import AppointmentSerializer, AppointmentCreateSerializer

from api.v1.appointment.serializers.appointment import TimeSerializer


class AppointmentsModelView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['appointments'])
    def get(self, request, format=None):
        apps = AppointmentsModel.objects.all()
        serializer = AppointmentSerializer(apps, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['appointments'], request_body=AppointmentCreateSerializer)
    def post(self, request, format=None):
        account = request.user
        app = AppointmentsModel(created_by=account, modified_by=account)
        serializer = AppointmentCreateSerializer(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            for i in serializer.data['services']:
                AppointmentServiceModel.objects.create(appointment=app, service_id=i['service'], created_by=account, modified_by=account)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentsRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AppointmentSerializer

    @staticmethod
    def get_queryset():
        return AppointmentsModel.objects.all()

    @swagger_auto_schema(tags=['appointments'])
    def get(self, request, pk, format=None):
        try:
            app = AppointmentsModel.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AppointmentSerializer(app)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['appointments'], request_body=AppointmentCreateSerializer)
    def put(self, request, pk, format=None):
        try:
            app = AppointmentsModel.objects.get(pk=pk)
            app.modified_by = request.user
            app.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentCreateSerializer(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['appointments'])
    def delete(self, request, pk, format=None):
        try:
            app = AppointmentsModel.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        app.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method="post", tags=["appointments"], request_body=TimeSerializer)
@api_view(['POST', ])
def appointment_time_view(request):
    min_date = request.data['min']
    max_date = request.data['max']
    appoints = AppointmentsModel.objects.filter(start_time__gte=min_date, end_time__lte=max_date)
    serializer = AppointmentSerializer(appoints, many=True)
    return Response(serializer.data)