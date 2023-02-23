from rest_framework import serializers
from apps.warehouse.models import IncomeItemsModel


class IncomeItemsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = IncomeItemsModel
        exclude = ["modified_by", "created_by"]