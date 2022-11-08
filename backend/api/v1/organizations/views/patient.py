from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from api.v1.organizations.serializers.patient import PatientModelSerializer, PatientCreateSerializer
from account.models.patients import PatientModel
from django.db.models import Q
from api.v1.organizations.serializers.patient import PatientSearchSerializer
from rest_framework.decorators import api_view


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


@swagger_auto_schema(method='post', tags=['patients'], request_body=PatientSearchSerializer)
@api_view(['POST'])
def filter_patients_view(request):
    data = request.data
    l_name = data['l_name']
    f_name = data['f_name']
    mid_name = data['mid_name']
    inn = data['inn']
    doc_number = data['doc_number']
    date_of_birth = data['date_of_birth']
    mobile_phone_number = data['mobile_phone_number']
    id = data['id']

    last_visit_at = data['last_visit_at']
    patients = PatientModel.objects.filter(Q(l_name=l_name) | Q(f_name=f_name) | Q(mid_name=mid_name) | Q(INN=inn)
                                           | Q(doc_number=doc_number) | Q(date_of_birth=date_of_birth) |
                                           Q(mobile_phone_number=mobile_phone_number) | Q(id=id) |
                                           Q(last_visit_at=last_visit_at))
    serializer = PatientModelSerializer(patients, many=True)
    return Response(data=serializer.data)









