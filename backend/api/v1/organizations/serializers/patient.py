from rest_framework import serializers
from account.models.patients import PatientModel


class PatientModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientModel
        fields = '__all__'


class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientModel
        fields = ['f_name',
                  'mid_name',
                  'l_name',
                  'home_phone_number',
                  'mobile_phone_number',
                  'address',
                  'INN',
                  'country',
                ]