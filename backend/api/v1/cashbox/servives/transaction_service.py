from rest_framework import status
from rest_framework.response import Response

from api.v1.cashbox.serializers import CreateTransactionSerializer, AppointmentServiceTransactionsCreateSerializer
from apps.account.models import AppointmentsModel
from apps.cashbox.models.transactions import AppointmentServiceTransactionsModel, TransactionsModel


def payment_proceed_service(request):
    payment = TransactionsModel(created_by=request.user, modified_by=request.user)
    serializer = CreateTransactionSerializer(payment, data=request.data)
    if serializer.is_valid():
        if not serializer.validated_data['is_manual']:
            appointment = AppointmentsModel.objects.get(id=serializer.validated_data['appointment_id'])
            serializer.validated_data['amount'] = appointment.price
        serializer.save()


        # save transaction service serializer
        for srv in serializer.validated_data['tr_srv']:
            transaction_service = AppointmentServiceTransactionsModel(transaction=payment)
            srv_serializer = AppointmentServiceTransactionsCreateSerializer(transaction_service, data=srv)
            if srv_serializer.is_valid():
                srv_serializer.save()

        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
