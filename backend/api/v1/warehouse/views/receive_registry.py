from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.v1.warehouse.serializers import ReceiveRegistryModelSerializer
from apps.warehouse.models import ReceiveRegistryModel


@permission_classes((IsAuthenticated, ))
@swagger_auto_schema(method="get", tags=["warehouse-receive-registry"])
@api_view(['GET'])
def get_receive_registry_view(request):
        receive_registry = ReceiveRegistryModel.objects.all()
        serializer = ReceiveRegistryModelSerializer(receive_registry, many=True)
        return Response(serializer.data)



@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="get", tags=["warehouse-receive-registry"])
@api_view(['GET'])
def get_receive_registry_retrieve_view(request, pk):
        receive_registry = get_object_or_404(ReceiveRegistryModel, pk=pk)
        serializer = ReceiveRegistryModelSerializer(receive_registry)
        return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="post", tags=["warehouse-receive-registry"], request_body=ReceiveRegistryModelSerializer)
@api_view(['POST'])
def create_receive_registry_view(request):
        receive_registry = ReceiveRegistryModel.objects.create(modified_by=request.user, created_by=request.user)
        serializer = ReceiveRegistryModelSerializer(receive_registry, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="put", tags=["warehouse-receive-registry"], request_body=ReceiveRegistryModelSerializer)
@api_view(['PUT'])
def update_receive_registry_view(request, pk):
        receive_registry = get_object_or_404(ReceiveRegistryModel, pk=pk)
        receive_registry.modified_by = request.user
        receive_registry.save()
        serializer = ReceiveRegistryModelSerializer(receive_registry, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="delete", tags=["warehouse-receive-registry"])
@api_view(['DELETE'])
def delete_receive_registry_view(request, pk):
        receive_registry = get_object_or_404(ReceiveRegistryModel, pk=pk)
        receive_registry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)