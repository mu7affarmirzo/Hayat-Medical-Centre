from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from apps.cashbox.models import TransactionsModel
from api.v1.appointment.serializers.appointment import TimeSerializer
from django.shortcuts import get_object_or_404
from api.v1.cashbox.serializers import TransactionsSerializer


class TransactionsView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['transactions'])
    def get(self, request, format=None):
        transactions = TransactionsModel.objects.all()
        serializer = TransactionsSerializer(transactions, many=True)
        return Response(serializer.data)
#
#     @swagger_auto_schema(tags=['cashbox'])
#     def post(self, request, format=None):
#
#         serializer = CashBoxSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
# class CashBoxRetrieveView(RetrieveAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = CashBoxSerializer
#
#
#     @swagger_auto_schema(tags=['cashbox'])
#     def get(self, request, pk, format=None):
#         cashbox = get_object_or_404(CashBoxClosingHistoryRecordsModel, pk=pk)
#         serializer = CashBoxSerializer(cashbox)
#         return Response(serializer.data)
#
#     @swagger_auto_schema(tags=['cashbox'])
#     def put(self, request, pk, format=None):
#         cashbox = get_object_or_404(CashBoxClosingHistoryRecordsModel, pk=pk)
#         serializer = CashBoxSerializer(cashbox, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     @swagger_auto_schema(tags=['cashbox'])
#     def delete(self, request, pk, format=None):
#         cashbox = get_object_or_404(CashBoxClosingHistoryRecordsModel, pk=pk)
#         cashbox.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
@swagger_auto_schema(method="post", tags=["transactions"], request_body=TimeSerializer)
@api_view(['POST', ])
def transactions_time_view(request):
    min_date = request.data['min']
    max_date = request.data['max']
    transactions = TransactionsModel.objects.filter(created_at__range=[min_date, max_date])
    serializer = TransactionsSerializer(transactions, many=True)
    return Response(serializer.data)