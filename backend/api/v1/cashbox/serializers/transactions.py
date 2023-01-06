from abc import ABC

from rest_framework import serializers
from apps.cashbox.models import TransactionsModel
from apps.cashbox.models.transactions import AppointmentServiceTransactionsModel


class TransactionsSerializer(serializers.ModelSerializer):
    receipt_id = serializers.SerializerMethodField('get_receipt_id')
    doctor = serializers.SerializerMethodField('get_doctor')
    specialty = serializers.SerializerMethodField('get_doctor_specialty')
    service = serializers.SerializerMethodField('get_service')
    patient = serializers.SerializerMethodField('get_patient')
    base_price = serializers.SerializerMethodField('get_base_price')

    class Meta:
        model = TransactionsModel
        fields = '__all__'

    def get_receipt_id(self, obj):
        return obj.receipt.id

    def get_doctor(self, obj):
        context = {}
        context['id'] = obj.receipt.receipt_appointments.first().doctor.doctor.id
        context['username'] = obj.receipt.receipt_appointments.first().doctor.doctor.username
        return context

    def get_doctor_specialty(self, obj):
        context = {}
        context['id'] = obj.receipt.receipt_appointments.first().doctor.doc_speciality.first().speciality.id
        context['name'] = obj.receipt.receipt_appointments.first().doctor.doc_speciality.first().speciality.name
        return context

    def get_service(self, obj):
        context = {}
        context['id'] = obj.receipt.receipt_appointments.first().app_services.first().service.id
        context['name'] = obj.receipt.receipt_appointments.first().app_services.first().service.name
        return context

    def get_patient(self, obj):
        context = {}
        context['id'] = obj.receipt.receipt_appointments.first().patient.id
        context['name'] = obj.receipt.receipt_appointments.first().patient.f_name
        return context

    def get_base_price(self, obj):
        return obj.receipt.receipt_appointments.first().price


class AppointmentServiceTransactionsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppointmentServiceTransactionsModel
        fields = '__all__'


class AppointmentServiceTransactionsSerializer(serializers.Serializer):
    service_id = serializers.CharField()
    # class Meta:
    #     model = AppointmentServiceTransactionsModel
    #     fields = [
    #         'service_id'
    #     ]


class CreateTransactionSerializer(serializers.ModelSerializer):
    tr_srv = AppointmentServiceTransactionsSerializer(many=True, read_only=True)

    class Meta:
        model = TransactionsModel
        fields = [
            "amount",
            "payment_type",
            "is_manual",
            "appointment_id",
            "tr_srv",
            "transaction_type",
            "receipt",
            "branch",
            "referring_doctor"
        ]

    # def update(self, instance, validated_data):
    #     services = validated_data.pop('tr_srv')
    #     for srv in services:
    #         AppointmentServiceTransactionsModel.objects.create(
    #             transaction=instance, service_id=srv['service_id'])
    #     return instance
