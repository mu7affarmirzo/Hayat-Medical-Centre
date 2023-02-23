from rest_framework import serializers
from apps.warehouse.models import IncomeModel


class IncomeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = IncomeModel
        exclude = ["modified_by", "created_by"]