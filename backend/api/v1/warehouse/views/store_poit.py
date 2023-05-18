from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.v1.warehouse.serializers import StorePointModelSerializer
from apps.warehouse.models import StorePointModel


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="get", tags=["warehouse-store-point"])
@api_view(['GET'])
def get_store_point_view(request):
    store_point = StorePointModel.objects.all()
    serializer = StorePointModelSerializer(store_point, many=True)
    return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="get", tags=["warehouse-store-point"])
@api_view(['GET'])
def get_store_point_retrieve_view(request, pk):
    store_point = get_object_or_404(StorePointModel, pk=pk)
    serializer = StorePointModelSerializer(store_point)
    return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="post", tags=["warehouse-store-point"], request_body=StorePointModelSerializer)
@api_view(['POST'])
def create_store_point_view(request):
    store_point = StorePointModel.objects.create(modified_by=request.user, created_by=request.user)
    serializer = StorePointModelSerializer(store_point, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="put", tags=["warehouse-store-point"], request_body=StorePointModelSerializer)
@api_view(['PUT'])
def update_store_point_view(request, pk):
    store_point = get_object_or_404(StorePointModel, pk=pk)
    store_point.modified_by = request.user
    store_point.save()
    serializer = StorePointModelSerializer(store_point, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="delete", tags=["warehouse-store-point"])
@api_view(['DELETE'])
def delete_store_point_view(request, pk):
    store_point = get_object_or_404(StorePointModel, pk=pk)
    store_point.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
