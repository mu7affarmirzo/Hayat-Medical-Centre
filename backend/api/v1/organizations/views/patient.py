from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework import filters
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from api.v1.organizations.serializers.patient import PatientModelSerializer, PatientCreateSerializer
from api.v1.organizations.services.filters import PatientFilter
from apps.account.models import PatientModel
from django.db.models import Q
from api.v1.organizations.serializers.patient import PatientSearchSerializer
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend


class PatientView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['patients'])
    def get(self, requset, format=None):
        patients = PatientModel.objects.all()
        serializer = PatientModelSerializer(patients, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['patients'], request_body=PatientCreateSerializer)
    def post(self, request, format=None):
        account = request.user
        patient = PatientModel(created_by=account, modified_by=account)
        serializer = PatientCreateSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientModelSerializer

    @staticmethod
    def get_queryset():
        return PatientModel.objects.all()

    @swagger_auto_schema(tags=['patients'])
    def get(self, request, pk, format=None):
        try:
            patient = PatientModel.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientModelSerializer(patient)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['patients'], request_body=PatientModelSerializer)
    def put(self, request, pk, format=None):
        try:
            patient = PatientModel.objects.get(pk=pk)
            patient.modified_by = request.user
            patient.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PatientCreateSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['patients'])
    def delete(self, request, pk, format=None):
        try:
            patient = PatientModel.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PatientFilterView(ListAPIView):
    queryset = PatientModel.objects.all()
    serializer_class = PatientModelSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = PatientFilter







