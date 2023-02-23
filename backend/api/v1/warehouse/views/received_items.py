from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.v1.warehouse.serializers import ReceivedItemsModelSerializer
from apps.warehouse.models import ReceivedItemsModel


@permission_classes((IsAuthenticated, ))
@swagger_auto_schema(method="get", tags=["warehouse-received-items"])
@api_view(['GET'])
def get_received_item_view(request):
        received_item = ReceivedItemsModel.objects.all()
        serializer = ReceivedItemsModelSerializer(received_item, many=True)
        return Response(serializer.data)



@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="get", tags=["warehouse-received-items"])
@api_view(['GET'])
def get_received_item_retrieve_view(request, pk):
        received_item = get_object_or_404(ReceivedItemsModel, pk=pk)
        serializer = ReceivedItemsModelSerializer(received_item)
        return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="post", tags=["warehouse-received-items"], request_body=ReceivedItemsModelSerializer)
@api_view(['POST'])
def create_received_item_view(request):
        received_item = ReceivedItemsModel.objects.create(modified_by=request.user, created_by=request.user)
        serializer = ReceivedItemsModelSerializer(received_item, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="put", tags=["warehouse-received-items"], request_body=ReceivedItemsModelSerializer)
@api_view(['PUT'])
def update_received_item_view(request, pk):
        received_item = get_object_or_404(ReceivedItemsModel, pk=pk)
        received_item.modified_by = request.user
        received_item.save()
        serializer = ReceivedItemsModelSerializer(received_item, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="delete", tags=["warehouse-received-items"])
@api_view(['DELETE'])
def delete_received_item_view(request, pk):
        received_item = get_object_or_404(ReceivedItemsModel, pk=pk)
        received_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)