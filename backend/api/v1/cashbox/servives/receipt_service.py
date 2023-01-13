from rest_framework import status
from rest_framework.response import Response

from api.v1.appointment.serializers.appointment import AppointmentCreateSerializer, AppointmentSerializer
from api.v1.cashbox.serializers import ReceiptCreateSerializer, ReceiptSerializer
from apps.account.models import AppointmentsModel, AppointmentServiceModel, MedicalService
from apps.cashbox.models import ReceiptModel


def create_receipt_service(request, account):
    sum_service_price = 0
    user = account
    receipt = ReceiptModel(created_by=user, modified_by=user)
    serializer = ReceiptCreateSerializer(receipt, data=request.data)
    appointments = []
    if serializer.is_valid():
        serializer.save()
        for appointment in serializer.data['appointments']:
            if not appointment["is_manual"]:
                for service in appointment['services']:
                    sum_service_price += MedicalService.objects.get(pk=service["service"]).cost
                    appointment.pop("price")
                app = AppointmentsModel(created_by=account, modified_by=account, receipt=receipt, price=sum_service_price)
            else:
                app = AppointmentsModel(created_by=account, modified_by=account, receipt=receipt)

            serializer = AppointmentCreateSerializer(app, data=appointment)
            if serializer.is_valid():
                serializer.save()
                for service in serializer.data['services']:
                    appointments.append(AppointmentServiceModel.objects.create(appointment=app,
                                                           service_id=service['service'],
                                                           quantity=service['quantity'],
                                                           created_by=account, modified_by=account))
        receipt_appointments  = AppointmentSerializer(appointments, many=True)
        r_serializer = ReceiptSerializer(receipt, receipt_appointments=receipt_appointments)
        return Response(r_serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
