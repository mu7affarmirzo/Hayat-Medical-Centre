from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

from api.v1.appointment.serializers.appointment import TimeSerializer
from api.v1.cashbox.serializers.receipt import ReceiptSerializer, ReceiptCreateSerializer, RetrieveReceiptSerializer
from api.v1.cashbox.servives.receipt_service import create_receipt_service
from apps.account.models import AppointmentsModel
from apps.cashbox.models import ReceiptModel
from django.shortcuts import get_object_or_404


class ReceiptView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReceiptSerializer

    @swagger_auto_schema(tags=['receipt'])
    def get(self, request, format=None):
        receipts = ReceiptModel.objects.all()
        serializer = ReceiptSerializer(receipts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['receipt'], request_body=ReceiptCreateSerializer)
    def post(self, request, format=None):
        user = request.user
        return create_receipt_service(request, user)


class ReceiptRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ReceiptModel.objects.all()
    serializer_class = ReceiptSerializer

    @swagger_auto_schema(tags=['receipt'])
    def get(self, request, pk, format=None):
        receipt = get_object_or_404(ReceiptModel, pk=pk)
        serializer = ReceiptSerializer(receipt)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['receipt'])
    def put(self, request, pk, format=None):
        receipt = get_object_or_404(ReceiptModel, pk=pk)
        receipt.modified_by = request.user
        receipt.save()
        serializer = ReceiptSerializer(receipt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['receipt'])
    def delete(self, request, pk, format=None):
        receipt = get_object_or_404(ReceiptModel, pk=pk)
        receipt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method="post", tags=["receipt"], request_body=TimeSerializer)
@api_view(['POST', ])
def receipt_time_view(request):
    min_date = request.data['min']
    max_date = request.data['max']
    receipt = ReceiptModel.objects.filter(created_at__range=[min_date, max_date])
    serializer = ReceiptSerializer(receipt, many=True)
    return Response(serializer.data)