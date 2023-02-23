from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.v1.warehouse.serializers import IncomeItemsModelSerializer
from apps.warehouse.models import IncomeItemsModel


@permission_classes((IsAuthenticated, ))
@swagger_auto_schema(method="get", tags=["warehouse-income-items"])
@api_view(['GET'])
def get_income_item_view(request):
        income_items = IncomeItemsModel.objects.all()
        serializer = IncomeItemsModelSerializer(income_items, many=True)
        return Response(serializer.data)



@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="get", tags=["warehouse-income-items"])
@api_view(['GET'])
def get_income_item_retrieve_view(request, pk):
        income_item = get_object_or_404(IncomeItemsModel, pk=pk)
        serializer = IncomeItemsModelSerializer(income_item)
        return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="post", tags=["warehouse-income-items"], request_body=IncomeItemsModelSerializer)
@api_view(['POST'])
def create_income_item_view(request):
        income_item = IncomeItemsModel.objects.create(created_by=request.user, modified_by=request.user)
        serializer = IncomeItemsModelSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="put", tags=["warehouse-income-items"], request_body=IncomeItemsModelSerializer)
@api_view(['PUT'])
def update_income_item_view(request, pk):
        income_item = get_object_or_404(IncomeItemsModel, pk=pk)
        income_item.modified_by = request.user
        income_item.save()
        serializer = IncomeItemsModelSerializer(income_item, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="delete", tags=["warehouse-income-items"])
@api_view(['DELETE'])
def delete_income_item_view(request, pk):
        income_item = get_object_or_404(IncomeItemsModel, pk=pk)
        income_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)