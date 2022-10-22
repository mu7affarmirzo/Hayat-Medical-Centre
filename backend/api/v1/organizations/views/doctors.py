from django.db.models import Exists, Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from account.models import DoctorSpecialityModel
from account.models.accounts import Account
from api.v1.organizations.serializers.doctors import DoctorsCreateSerializer


class DoctorsListCreateView(APIView):

    @staticmethod
    def get_queryset():
        return Account.objects.filter(doc_speciality__isnull=False)

    @swagger_auto_schema(tags=['organizations'])
    @permission_classes((IsAuthenticated,))
    def get(self, request, format=None):
        doctors = self.get_queryset()
        serializer = DoctorsCreateSerializer(doctors, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['organizations'], request_body=DoctorsCreateSerializer)
    @permission_classes((IsAuthenticated, ))
    def post(self, request, format=None):
        serializer = DoctorsCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorsRetrieveView(RetrieveUpdateDestroyAPIView):

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset()

    def get_object(self):
        return super().get_object()

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)