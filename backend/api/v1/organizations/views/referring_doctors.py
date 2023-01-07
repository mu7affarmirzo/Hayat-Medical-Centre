from drf_yasg.utils import swagger_auto_schema
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from apps.account.models import ReferringDoctorModel
from api.v1.organizations.serializers import ReferringDoctorsListSerializer, ReferringDoctorsCreateSerializer


class ReferringDoctorsView(APIView):

    @swagger_auto_schema(tags=['organizations-referring-doctors'])
    def get(self, request):
        referring_doctors = ReferringDoctorModel.objects.all()
        serializer = ReferringDoctorsListSerializer(referring_doctors, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['organizations-referring-doctors'], request_body=ReferringDoctorsCreateSerializer)
    @permission_classes((IsAuthenticated,))
    def post(self, request):
        creator = request.user
        specialty = ReferringDoctorModel(created_by=creator)
        serializer = ReferringDoctorsListSerializer(specialty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
