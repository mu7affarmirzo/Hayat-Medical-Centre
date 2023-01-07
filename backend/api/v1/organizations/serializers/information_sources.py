from rest_framework import serializers
from apps.account.models import InformationSourceModel


class InformationSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationSourceModel
        fields = '__all__'


class InformationSourceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationSourceModel
        fields = ['name', 'organization']

