from apps.account.models import AppointmentsModel, AppointmentServiceModel, MedicalService
from rest_framework import serializers
from django.shortcuts import get_object_or_404

class AppointmentServiceSerializers(serializers.ModelSerializer):
    service_name = serializers.SerializerMethodField()

    class Meta:
        model = AppointmentServiceModel
        fields = '__all__'

    def get_service_name(self, obj):
        return obj.service.name


class AppointmentServiceCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = AppointmentServiceModel
        fields = ['service', 'quantity']


class AppointmentSerializer(serializers.ModelSerializer):
    services = AppointmentServiceSerializers(many=True, source='app_services')
    patient_name = serializers.SerializerMethodField()
    patient_birth_date = serializers.SerializerMethodField()
    doctor_name = serializers.SerializerMethodField()

    class Meta:
        model = AppointmentsModel
        fields = [
            'id',
            'patient',
            'patient_name',
            'patient_birth_date',
            'name',
            'discount',
            'start_time',
            'end_time',
            'price',
            'debt',
            'referring_doctor',
            'information_source',
            'referring_doc_notes',
            'addition_info',
            'branch',
            'services',
            'doctor',
            'doctor_name'
        ]

    def get_patient_name(self, obj):
        name = "Unknown"
        try:
            name = obj.patient.full_name
        except:
            pass
        return name

    def get_patient_birth_date(self, obj):
        date_of_birth = "Unknown"
        try:
            date_of_birth = obj.patient.date_of_birth
        except:
            pass
        return date_of_birth

    def get_doctor_name(self, obj):
        name = "Unknown"
        try:
            name = obj.doctor.doctor.full_name
        except:
            pass
        return name


class AppointmentCreateSerializer(serializers.ModelSerializer):
    services = AppointmentServiceCreateSerializers(many=True)

    class Meta:
        model = AppointmentsModel
        fields = [
                  'patient',
                  'name',
                  'discount',
                  'start_time',
                  'end_time',
                  'referring_doctor',
                  'information_source',
                  'referring_doc_notes',
                  'addition_info',
                  'price',
                  'is_manual',
                  'branch',
                  'services',
                  'doctor'
                  ]

    def create(self, validated_data):
        """
        This is not working
        """
        services = validated_data.pop('services')
        appointment = AppointmentsModel.objects.create(**validated_data)

        for service in services:
            AppointmentServiceModel.objects.create(appointment=appointment,
                                                   service=1, doctor=appointment.doctor, **service)
        return appointment

    # def update(self, instance, validated_data):
    #     instance.price = 0
    #     if validated_data["is_manual"]:
    #         instance.price = validated_data["price"]
    #     else:
    #         for service in validated_data["services"]:
    #             print(100*"0", dict(service.items())["service"].cost)
    #             instance.price += dict(service.items())["service"].cost
    #         # instance.price = sum_services_price
    #     instance.save()


class TimeSerializer(serializers.Serializer):
    min = serializers.DateTimeField()
    max = serializers.DateTimeField()

    class Meta:
        fields = '__all__'
