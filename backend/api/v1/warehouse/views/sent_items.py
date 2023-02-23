from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.v1.warehouse.serializers import SentItemsModelSerializer
from apps.warehouse.models import SentItemsModel


@permission_classes((IsAuthenticated, ))
@swagger_auto_schema(method="get", tags=["warehouse-sent-items"])
@api_view(['GET'])
def get_sent_items_view(request):
        sent_items = SentItemsModel.objects.all()
        serializer = SentItemsModelSerializer(sent_items, many=True)
        return Response(serializer.data)



@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="get", tags=["warehouse-sent-items"])
@api_view(['GET'])
def get_sent_items_retrieve_view(request, pk):
        sent_items = get_object_or_404(SentItemsModel, pk=pk)
        serializer = SentItemsModelSerializer(sent_items)
        return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="post", tags=["warehouse-sent-items"], request_body=SentItemsModelSerializer)
@api_view(['POST'])
def create_sent_items_view(request):
        sent_items = SentItemsModel.objects.create(modified_by=request.user, created_by=request.user)
        serializer = SentItemsModelSerializer(sent_items, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="put", tags=["warehouse-sent-items"], request_body=SentItemsModelSerializer)
@api_view(['PUT'])
def update_sent_items_view(request, pk):
        sent_items = get_object_or_404(SentItemsModel, pk=pk)
        sent_items.modified_by = request.user
        sent_items.save()
        serializer = SentItemsModelSerializer(sent_items, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated,))
@swagger_auto_schema(method="delete", tags=["warehouse-sent-items"])
@api_view(['DELETE'])
def delete_sent_items_view(request, pk):
        sent_items = get_object_or_404(SentItemsModel, pk=pk)
        sent_items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)