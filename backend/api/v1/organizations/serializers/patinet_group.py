from rest_framework import serializers
from account.models.patients import PatientGroupModel


class PatientGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientGroupModel
        fields = '__all__'


class PatientGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientGroupModel
        fields = ['name', 'color', 'exemption_percentage', 'organization']

