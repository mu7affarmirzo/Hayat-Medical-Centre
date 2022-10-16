from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import SpecialityModel
from api.v1.organizations.serializers.specialties import SpecialtiesListSerializer
from rest_framework.generics import ListAPIView


class SpecialtiesView(APIView):

    @swagger_auto_schema(tags=['organizations'])
    def get(self, request, format=None):
        specialities = SpecialityModel.objects.all()
        serializer = SpecialtiesListSerializer(specialities, many=True)
        return Response(serializer.data)

