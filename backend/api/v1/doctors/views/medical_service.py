from apps.account.models import MedicalService
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

from api.v1.doctors.serializers.medical_service import MedicalServiceSerializer, MedicalServiceCreateSerializer
from django.db.models import Q
from rest_framework.decorators import api_view


class MedicalServiceView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['medical-services'])
    def get(self, requset, format=None):
        service = MedicalService.objects.all()
        serializer = MedicalServiceSerializer(service, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['medical-services'], request_body=MedicalServiceCreateSerializer)
    def post(self, request, format=None):
        account = request.user
        service = MedicalService(created_by=account, modified_by=account)
        serializer = MedicalServiceCreateSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicalServiceRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MedicalServiceSerializer

    def get_queryset(self):
        return MedicalService.objects.all()

    @swagger_auto_schema(tags=['medical-services'])
    def get(self, request, pk, format=None):
        try:
            service = MedicalService.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MedicalServiceSerializer(service)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['medical-services'], request_body=MedicalServiceCreateSerializer)
    def put(self, request, pk, format=None):
        try:
            service = MedicalService.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MedicalServiceCreateSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['medical-services'])
    def delete(self, request, pk, format=None):
        try:
            service = MedicalService.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
