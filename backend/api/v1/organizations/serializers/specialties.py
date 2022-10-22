from rest_framework import serializers

from account.models import SpecialityModel, DoctorSpecialityModel


class SpecialtiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialityModel
        fields = [
            'id',
            "name",
            "color"
        ]


class SpecialtiesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialityModel
        fields = "__all__"

