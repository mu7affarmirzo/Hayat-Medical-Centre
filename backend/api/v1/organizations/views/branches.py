from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.organizations.serializers.doctors import DoctorsListSerializer
from api.v1.organizations.serializers.specialties import SpecialitiesListSerializer, DoctorSpecialitiesListSerializer
from apps.account.models import PatientModel, Account, SpecialityModel, DoctorSpecialityModel


@swagger_auto_schema(tags=['organizations'], method="get")
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def doctors_by_branch_view(request, branch_id):
    # doc_specs = DoctorSpecialityModel.objects.filter(branch=branch_id).distinct('doctor')
    ###
    doc_specs = Account.objects.filter(branch_id=branch_id)
    ###
    # print(doc_specs)
    # doctors = Account.objects.filter(doctorspecialitymodel__in=doc_specs)
    # print("************")
    # print(doctors)
    # print("************")
    # TODO: finish this part
    # serializer = DoctorSpecialitiesListSerializer(doc_specs, many=True)
    ###
    serializer = DoctorsListSerializer(doc_specs, many=True)
    ###

    return Response(serializer.data)


@swagger_auto_schema(tags=['branch-speciality'], methods=['get', ])
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def specialty_by_branch_view(request, pk):
    specialties = SpecialityModel.objects.filter(branch=pk)
    serializer = SpecialitiesListSerializer(specialties, many=True)
    return Response(serializer.data)


@swagger_auto_schema(tags=['branch-speciality'], methods=['get', ])
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_specialty_by_id_view(request, pk, spec_id):
    specialty = get_object_or_404(SpecialityModel, branch=pk, id=spec_id)
    doctors = Account.objects.filter(doctorspecialitymodel__speciality=specialty)

    serializer = DoctorsListSerializer(doctors, many=True)
    return Response(serializer.data)
