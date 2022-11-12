from django.db.models import Exists, Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.account.models import DoctorSpecialityModel
from apps.account.models import Account
from api.v1.organizations.serializers.doctors import DoctorsCreateSerializer, DoctorsListSerializer, \
    DoctorSearchSerializer


class DoctorsListCreateView(APIView):

    @staticmethod
    def get_queryset():
        return Account.objects.filter(doc_speciality__isnull=False)

    @swagger_auto_schema(tags=['organizations-doctor'])
    @permission_classes((IsAuthenticated,))
    def get(self, request, format=None):
        doctors = self.get_queryset()
        serializer = DoctorsListSerializer(doctors, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['organizations-doctor'], request_body=DoctorsCreateSerializer)
    @permission_classes((IsAuthenticated, ))
    def post(self, request, format=None):
        serializer = DoctorsCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorsRetrieveView(RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = DoctorsListSerializer

    def get_queryset(self):
        return super().get_queryset()

    @swagger_auto_schema(tags=['organizations-doctor'])
    def get(self, request, pk, format=None):
        try:
            doctor = Account.objects.filter(doc_speciality__isnull=False, pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DoctorsListSerializer(doctor)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['organizations-doctor'], request_body=DoctorsListSerializer)
    def put(self, request, pk, format=None):
        doctor = Account.objects.filter(doc_speciality__isnull=False, pk=pk)

        serializer = DoctorsListSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['organizations-doctor'])
    def delete(self, request, pk, format=None):
        doctor = Account.objects.filter(doc_speciality__isnull=False, pk=pk)

        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

