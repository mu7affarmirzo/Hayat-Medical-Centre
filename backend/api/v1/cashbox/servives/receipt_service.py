from rest_framework import status
from rest_framework.response import Response

from api.v1.appointment.serializers.appointment import AppointmentCreateSerializer
from api.v1.cashbox.serializers import ReceiptCreateSerializer
from apps.account.models import AppointmentsModel, AppointmentServiceModel
from apps.cashbox.models import ReceiptModel


def create_receipt_service(request, account):
    user = account
    receipt = ReceiptModel(created_by=user, modified_by=user)
    serializer = ReceiptCreateSerializer(receipt, data=request.data)
    if serializer.is_valid():
        serializer.save()
        for appointment in serializer.data['appointments']:

            app = AppointmentsModel(created_by=account, modified_by=account, receipt=receipt)
            serializer = AppointmentCreateSerializer(app, data=appointment)
            if serializer.is_valid():
                serializer.save()
                for service in serializer.data['services']:
                    AppointmentServiceModel.objects.create(appointment=app,
                                                           service_id=service['service'],
                                                           doctor=app.doctor,
                                                           created_by=account, modified_by=account)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
