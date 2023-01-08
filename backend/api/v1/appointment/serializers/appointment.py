from apps.account.models import AppointmentsModel, AppointmentServiceModel
from rest_framework import serializers


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
    doctor_name = serializers.SerializerMethodField()

    class Meta:
        model = AppointmentsModel
        fields = [
            'id',
            'patient',
            'patient_name',
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
        return obj.patient.full_name

    def get_doctor_name(self, obj):
        return obj.doctor.doctor.full_name


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


class TimeSerializer(serializers.Serializer):
    min = serializers.DateTimeField()
    max = serializers.DateTimeField()

    class Meta:
        fields = '__all__'
