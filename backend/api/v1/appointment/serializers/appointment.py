from apps.account.models import AppointmentsModel, AppointmentServiceModel
from rest_framework import serializers


class AppointmentServiceSerializers(serializers.ModelSerializer):

    class Meta:
        model = AppointmentServiceModel
        fields = '__all__'


class AppointmentServiceCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = AppointmentServiceModel
        fields = ['service', 'quantity']


class AppointmentSerializer(serializers.ModelSerializer):
    services = AppointmentServiceSerializers(many=True, source='app_services')

    class Meta:
        model = AppointmentsModel
        fields = [
            'id',
            'patient',
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
            'doctor'
        ]


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
