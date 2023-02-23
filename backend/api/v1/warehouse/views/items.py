from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.v1.warehouse.serializers import ItemsModelSerializer
from apps.warehouse.models import ItemsModel


@permission_classes((IsAuthenticated, ))
@swagger_auto_schema(method="get", tags=["warehouse-items"])
@api_view(['GET'])
def get_item_view(request):
        items = ItemsModel.objects.all()
        serializer = ItemsModelSerializer(items, many=True)
        return Response(serializer.data)



@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="get", tags=["warehouse-items"])
@api_view(['GET'])
def get_item_retrieve_view(request, pk):
        item = get_object_or_404(ItemsModel, pk=pk)
        serializer = ItemsModelSerializer(item)
        return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="post", tags=["warehouse-items"], request_body=ItemsModelSerializer)
@api_view(['POST'])
def create_item_view(request):
        serializer = ItemsModelSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="put", tags=["warehouse-items"], request_body=ItemsModelSerializer)
@api_view(['PUT'])
def update_item_view(request, pk):
        item = get_object_or_404(ItemsModel, pk=pk)
        serializer = ItemsModelSerializer(item, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="delete", tags=["warehouse-items"])
@api_view(['DELETE'])
def delete_item_view(request, pk):
        item = get_object_or_404(ItemsModel, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)