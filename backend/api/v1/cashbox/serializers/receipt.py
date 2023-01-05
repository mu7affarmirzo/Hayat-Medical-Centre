from rest_framework import serializers

from api.v1.appointment.serializers.appointment import AppointmentCreateSerializer, AppointmentSerializer, \
    AppointmentServiceSerializers
from apps.account.models import AppointmentsModel, AppointmentServiceModel
from apps.cashbox.models import ReceiptModel


# class ReceiptAppointmentSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = AppointmentsModel
#         fields = '__all__'

class RetrieveReceiptSerializer(serializers.ModelSerializer):
    receipt_appointments = AppointmentSerializer(many=True)
    services = serializers.SerializerMethodField('get_services_from_appointment')

    class Meta:
        model = ReceiptModel
        fields = [
            'id',
            # 'patient',
            # 'doctor',
            'services',
            'receipt_appointments'
            # 'doctor',
            # 'doctor',
            # ''
        ]

    def get_services_from_appointment(self, receipt):
        retrieved_services = []
        appointments = receipt.receipt_appointments.all()
        for app in appointments:
            services = app.app_services.all()
            for service in services:

                retrieved_services.append({
                    "doctor": service.doctor.id,
                    "service": service.service.id,
                    "quantity": service.quantity
                })
        return retrieved_services


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

