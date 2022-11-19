from apps.account.models import AppointmentsModel, AppointmentServiceModel
from rest_framework import serializers


class AppointmentServiceSerializers(serializers.ModelSerializer):

    class Meta:
        model = AppointmentServiceModel
        fields = '__all__'


class AppointmentServiceCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = AppointmentServiceModel
        fields = ['service']


class AppointmentSerializer(serializers.ModelSerializer):
    services = AppointmentServiceSerializers(many=True, source='app_services')

    class Meta:
        model = AppointmentsModel
        fields = [
            'patient',
            'name',
            'status',
            'exemption',
            'start_time',
            'end_time',
            'price',
            'debt',
            'referring_doctor',
            'information_source',
            'referring_doc_notes',
            'addition_info',
            'branch',
            'services'
        ]



class AppointmentCreateSerializer(serializers.ModelSerializer):
    services = AppointmentServiceCreateSerializers(many=True)

    class Meta:
        model = AppointmentsModel
        fields = ['patient',
                  'name',
                  'status',
                  'exemption',
                  'start_time',
                  'end_time',
                  'price',
                  'debt',
                  'referring_doctor',
                  'information_source',
                  'referring_doc_notes',
                  'addition_info',
                  'branch',
                  'services'
                  ]

    def create(self, validated_data):
        appointment_data = validated_data.pop('appointment')
        appointment = AppointmentsModel.objects.create(**validated_data)
        AppointmentServiceModel.objects.create(appointment=appointment, **appointment_data)
        return appointment


class TimeSerializer(serializers.Serializer):
    min = serializers.DateTimeField()
    max = serializers.DateTimeField()

    class Meta:
        fields = '__all__'
