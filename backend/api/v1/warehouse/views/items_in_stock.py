from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.v1.warehouse.serializers import ItemsInStockModelSerializer
from apps.warehouse.models import ItemsInStockModel


@permission_classes((IsAuthenticated, ))
@swagger_auto_schema(method="get", tags=["warehouse-items-in-stock"])
@api_view(['GET'])
def get_item_in_stock_view(request):
        items_in_stock = ItemsInStockModel.objects.all()
        serializer = ItemsInStockModelSerializer(items_in_stock, many=True)
        return Response(serializer.data)



@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="get", tags=["warehouse-items-in-stock"])
@api_view(['GET'])
def get_item_in_stock_retrieve_view(request, pk):
        item_in_stock = get_object_or_404(ItemsInStockModel, pk=pk)
        serializer = ItemsInStockModelSerializer(item_in_stock)
        return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="post", tags=["warehouse-items-in-stock"], request_body=ItemsInStockModelSerializer)
@api_view(['POST'])
def create_item_in_stock_view(request):
        serializer = ItemsInStockModelSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="put", tags=["warehouse-items-in-stock"], request_body=ItemsInStockModelSerializer)
@api_view(['PUT'])
def update_item_in_stock_view(request, pk):
        item_in_stock = get_object_or_404(ItemsInStockModel, pk=pk)
        serializer = ItemsInStockModelSerializer(item_in_stock, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="delete", tags=["warehouse-items-in-stock"])
@api_view(['DELETE'])
def delete_item_in_stock_view(request, pk):
        item_in_stock = get_object_or_404(ItemsInStockModel, pk=pk)
        item_in_stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)