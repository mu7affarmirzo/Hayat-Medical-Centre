from rest_framework import serializers

from account.models import MedicalService


class MedicalServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalService
        fields = '__all__'


class MedicalServiceCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalService
        fields = ['name',
                  'cost',
                  'doctor',
                  'speciality',
                  'branch',
                  ]