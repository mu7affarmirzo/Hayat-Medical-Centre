from account.models import AppointmentsModel, AppointmentServiceModel
from rest_framework import serializers


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentsModel
        fields = '__all__'


class AppointmentCreateSerializer(serializers.ModelSerializer):
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
                  ]


class AppointmentServiceSerializers(serializers.ModelSerializer):

    class Meta:
        model = AppointmentServiceModel
        fields = '__all__'


class AppointmentServiceCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = AppointmentServiceModel
        fields = ['branch', 'appointment', 'service']