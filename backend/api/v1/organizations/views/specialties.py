from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from account.models import SpecialityModel
from api.v1.organizations.serializers.specialties import SpecialtiesListSerializer
from rest_framework.generics import ListAPIView


class SpecialtiesView(APIView):

    @swagger_auto_schema(tags=['organizations'])
    def get(self, request, format=None):
        specialities = SpecialityModel.objects.all()
        serializer = SpecialtiesListSerializer(specialities, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['organizations'])
    @permission_classes((IsAuthenticated, ))
    def post(self, request, format=None):
        creator = request.user
        specialty = SpecialityModel(created_by=creator)
        serializer = SpecialtiesListSerializer(specialty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
