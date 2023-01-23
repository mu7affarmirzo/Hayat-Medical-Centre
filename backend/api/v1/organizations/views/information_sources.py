from apps.account.models import InformationSourceModel
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from api.v1.organizations.serializers.information_sources import InformationSourceSerializer, InformationSourceCreateSerializer
from rest_framework.generics import RetrieveAPIView


class InformationSourceView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = InformationSourceSerializer

    @swagger_auto_schema(tags=['information-sources'])
    def get(self, requset, format=None):
        patients = InformationSourceModel.objects.all()
        serializer = InformationSourceSerializer(patients, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['information-sources'], request_body=InformationSourceCreateSerializer)
    def post(self, request, format=None):
        account = request.user
        patient_group = InformationSourceModel(created_by=account, modified_by=account)
        serializer = InformationSourceSerializer(patient_group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InformationSourceRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = InformationSourceSerializer

    @staticmethod
    def get_queryset():
        return InformationSourceModel.objects.all()

    @swagger_auto_schema(tags=['information-sources'])
    def get(self, request, pk, format=None):
        try:
            patient_group = InformationSourceModel.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InformationSourceSerializer(patient_group)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['information-sources'], request_body=InformationSourceSerializer)
    def put(self, request, pk, format=None):
        try:
            patient_group = InformationSourceModel.objects.get(pk=pk)
            patient_group.modified_by = request.user
            patient_group.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InformationSourceCreateSerializer(patient_group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['information-sources'])
    def delete(self, request, pk, format=None):
        try:
            patient_group = InformationSourceModel.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        patient_group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
