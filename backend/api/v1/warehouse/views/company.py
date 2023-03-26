from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.v1.warehouse.serializers import CompanyModelSerializer
from apps.warehouse.models import CompanyModel


@permission_classes((IsAuthenticated, ))
@swagger_auto_schema(method="get", tags=["warehouse-company"])
@api_view(['GET'])
def get_company_view(request):
        companies = CompanyModel.objects.all()
        serializer = CompanyModelSerializer(companies, many=True)

        return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="get", tags=["warehouse-company"])
@api_view(['GET'])
def get_company_retrieve_view(request, pk):
        company = get_object_or_404(CompanyModel, pk=pk)
        serializer = CompanyModelSerializer(company)
        return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="post", tags=["warehouse-company"], request_body=CompanyModelSerializer)
@api_view(['POST'])
def create_company_view(request):
        serializer = CompanyModelSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="put", tags=["warehouse-company"], request_body=CompanyModelSerializer)
@api_view(['PUT'])
def update_company_view(request, pk):
        company = get_object_or_404(CompanyModel, pk=pk)
        serializer = CompanyModelSerializer(company, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="delete", tags=["warehouse-company"])
@api_view(['DELETE'])
def delete_company_view(request, pk):
        company = get_object_or_404(CompanyModel, pk=pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
