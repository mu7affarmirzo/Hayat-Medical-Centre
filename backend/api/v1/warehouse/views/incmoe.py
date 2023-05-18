from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.v1.warehouse.serializers import IncomeModelSerializer
from apps.warehouse.models import IncomeModel


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="get", tags=["warehouse-income"])
@api_view(['GET'])
def get_income_view(request):
    incomes = IncomeModel.objects.all()
    serializer = IncomeModelSerializer(incomes, many=True)
    return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="get", tags=["warehouse-income"])
@api_view(['GET'])
def get_income_retrieve_view(request, pk):
    income = get_object_or_404(IncomeModel, pk=pk)
    serializer = IncomeModelSerializer(income)
    return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="post", tags=["warehouse-income"], request_body=IncomeModelSerializer)
@api_view(['POST'])
def create_income_view(request):
    income = IncomeModel.objects.create(modified_by=request.user, created_by=request.user)
    serializer = IncomeModelSerializer(income, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="put", tags=["warehouse-income"], request_body=IncomeModelSerializer)
@api_view(['PUT'])
def update_income_view(request, pk):
    income = get_object_or_404(IncomeModel, pk=pk)
    income.created_by = request.user
    income.save()
    serializer = IncomeModelSerializer(income, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="delete", tags=["warehouse-income"])
@api_view(['DELETE'])
def delete_income_view(request, pk):
    income = get_object_or_404(IncomeModel, pk=pk)
    income.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
