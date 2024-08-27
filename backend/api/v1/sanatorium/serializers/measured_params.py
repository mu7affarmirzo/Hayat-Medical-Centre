from apps.sanatorium.models import (
    ArterialPressureModel,
    GlucometerModel,
    PulseModel,
    SaturationModel,
    TemperatureModel
)

from rest_framework import serializers


class ArterialPressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArterialPressureModel
        fields = '__all__'


class GlucometerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlucometerModel
        fields = '__all__'


class PulseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PulseModel
        fields = '__all__'


class SaturationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaturationModel
        fields = '__all__'


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureModel
        fields = '__all__'

