from rest_framework import serializers

from apps.account.models import SpecialityModel, DoctorSpecialityModel


# class CreateSerializer(serializers.ModelSerializer):
#
#     class

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


class DoctorSpecialitiesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorSpecialityModel
        fields = "__all__"


class DoctorSpecialitiesCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorSpecialityModel
        fields = "__all__"
        