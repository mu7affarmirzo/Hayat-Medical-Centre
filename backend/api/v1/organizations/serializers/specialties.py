from rest_framework import serializers

from api.v1.organizations.serializers.doctors import DoctorsListSerializer
from apps.account.models import SpecialityModel, DoctorSpecialityModel


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
    doctor = DoctorsListSerializer()
    specialty_name = serializers.SerializerMethodField()

    class Meta:
        model = DoctorSpecialityModel
        fields = "__all__"
        ordering = ('doctor__f_name',)

    def get_specialty_name(self, obj):
        try:
            specialty_name = str(obj.speciality.name)
        except:
            specialty_name = ''
        return specialty_name


class DoctorSpecialitiesCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorSpecialityModel
        fields = "__all__"
        ordering = ('name',)


class SpecialitiesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecialityModel
        fields = "__all__"
        ordering = ('name',)


