from account.models.patients import PatientGroupModel
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from api.v1.organizations.serializers.patinet_group import PatientGroupSerializer, PatientGroupCreateSerializer
from rest_framework.generics import RetrieveAPIView


class PatientGroupView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientGroupSerializer

    @swagger_auto_schema(tags=['patients-group'])
    def get(self, requset, format=None):
        patients = PatientGroupModel.objects.all()
        serializer = PatientGroupSerializer(patients, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['patients-group'], request_body=PatientGroupCreateSerializer)
    def post(self, request, format=None):
        account = request.user
        patient_group = PatientGroupModel(created_by=account, modified_by=account)
        serializer = PatientGroupSerializer(patient_group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientGroupRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientGroupSerializer

    @staticmethod
    def get_queryset():
        return PatientGroupModel.objects.all()

    @swagger_auto_schema(tags=['patients-group'])
    def get(self, request, pk, format=None):
        try:
            patient_group = PatientGroupModel.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientGroupSerializer(patient_group)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['patients-group'], request_body=PatientGroupSerializer)
    def put(self, request, pk, format=None):
        try:
            patient_group = PatientGroupModel.objects.get(pk=pk)
            patient_group.modified_by = request.user
            patient_group.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PatientGroupCreateSerializer(patient_group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['patients-group'])
    def delete(self, request, pk, format=None):
        try:
            patient_group = PatientGroupModel.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        patient_group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
