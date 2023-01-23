from rest_framework import status
from rest_framework.response import Response

from api.v1.cashbox.serializers import CreateTransactionSerializer, AppointmentServiceTransactionsCreateSerializer
from apps.account.models import AppointmentsModel
from apps.cashbox.models.transactions import AppointmentServiceTransactionsModel, TransactionsModel, DutyModel


def payment_proceed_service(request):
    try:
        duty = DutyModel.objects.get(created_by=request.user, is_closed=False)
    except DutyModel.DoesNotExist:
        duty = DutyModel.objects.create(created_by=request.user)
        duty.save()
    except DutyModel.MultipleObjectsReturned:
        duty = DutyModel.objects.filter(created_by=request.user, is_closed=False)
        duty = duty.first()

    payment = TransactionsModel(created_by=request.user, modified_by=request.user, duty=duty)
    serializer = CreateTransactionSerializer(payment, data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
