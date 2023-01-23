from rest_framework import serializers
from apps.account.models import ReferringDoctorModel


class ReferringDoctorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferringDoctorModel
        fields = "__all__"


class ReferringDoctorsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferringDoctorModel
        fields = "__all__"
