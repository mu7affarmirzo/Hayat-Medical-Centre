from rest_framework import serializers

from api.v1.organizations.serializers.doctors import DoctorsListSerializer
from apps.account.models import MedicalService


class MedicalServiceSerializer(serializers.ModelSerializer):
    doctor = DoctorsListSerializer(many=True)

    class Meta:
        model = MedicalService
        fields = '__all__'


class MedicalServiceCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalService
        fields = [
            'name',
            'cost',
            'doctor',
            'speciality',
            'branch',
        ]
