from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.v1.warehouse.serializers import SendRegistryModelSerializer
from apps.warehouse.models import SendRegistryModel


@permission_classes((IsAuthenticated, ))
@swagger_auto_schema(method="get", tags=["warehouse-send-registry"])
@api_view(['GET'])
def get_send_registry_view(request):
        send_registry = SendRegistryModel.objects.all()
        serializer = SendRegistryModelSerializer(send_registry, many=True)
        return Response(serializer.data)



@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="get", tags=["warehouse-send-registry"])
@api_view(['GET'])
def get_send_registry_retrieve_view(request, pk):
        send_registry = get_object_or_404(SendRegistryModel, pk=pk)
        serializer = SendRegistryModelSerializer(send_registry)
        return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="post", tags=["warehouse-send-registry"], request_body=SendRegistryModelSerializer)
@api_view(['POST'])
def create_send_registry_view(request):
        send_registry = SendRegistryModel.objects.create(modified_by=request.user, created_by=request.user)
        serializer = SendRegistryModelSerializer(send_registry, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="put", tags=["warehouse-send-registry"], request_body=SendRegistryModelSerializer)
@api_view(['PUT'])
def update_send_registry_view(request, pk):
        send_registry = get_object_or_404(SendRegistryModel, pk=pk)
        send_registry.modified_by = request.user
        send_registry.save()
        serializer = SendRegistryModelSerializer(send_registry, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="delete", tags=["warehouse-send-registry"])
@api_view(['DELETE'])
def delete_send_registry_view(request, pk):
        send_registry = get_object_or_404(SendRegistryModel, pk=pk)
        send_registry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)