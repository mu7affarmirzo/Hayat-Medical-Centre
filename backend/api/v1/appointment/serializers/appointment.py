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

    # days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = AppointmentsModel
        fields = [
            # 'days_since_joined',
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

    # def get_days_since_joined(self, validated_data):
    #     return validated_data.pop('services')

    def create(self, validated_data):
        services = validated_data.pop('services')
        appointment = AppointmentsModel.objects.create(**validated_data)
        for service in services:
            AppointmentServiceModel.objects.create(appointment=1, service=1, **service)
        return appointment


class TimeSerializer(serializers.Serializer):
    min = serializers.DateTimeField()
    max = serializers.DateTimeField()

    class Meta:
        fields = '__all__'
