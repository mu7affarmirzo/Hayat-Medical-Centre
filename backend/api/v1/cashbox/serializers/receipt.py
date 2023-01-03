from rest_framework import serializers

from api.v1.appointment.serializers.appointment import AppointmentCreateSerializer, AppointmentSerializer
from apps.account.models import AppointmentsModel, AppointmentServiceModel
from apps.cashbox.models import ReceiptModel


class ReceiptSerializer(serializers.ModelSerializer):
    receipt_appointments = AppointmentSerializer(many=True)

    class Meta:
        model = ReceiptModel
        fields = '__all__'


class ReceiptCreateSerializer(serializers.ModelSerializer):
    appointments = AppointmentCreateSerializer(many=True)

    class Meta:
        model = ReceiptModel
        fields = [
                  'appointments'
                  ]

