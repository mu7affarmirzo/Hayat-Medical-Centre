from rest_framework import serializers

from apps.warehouse.models import CompanyModel


class CompanyModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyModel
        fields = '__all__'