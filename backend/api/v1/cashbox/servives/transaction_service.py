from rest_framework import status
from rest_framework.response import Response

from api.v1.cashbox.serializers import CreateTransactionSerializer, AppointmentServiceTransactionsCreateSerializer
from apps.account.models import AppointmentsModel
from apps.cashbox.models.transactions import AppointmentServiceTransactionsModel, TransactionsModel


def payment_proceed_service(request):
    payment = TransactionsModel(created_by=request.user, modified_by=request.user)
    serializer = CreateTransactionSerializer(payment, data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
