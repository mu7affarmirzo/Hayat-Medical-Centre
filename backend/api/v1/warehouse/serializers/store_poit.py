from rest_framework import serializers
from apps.warehouse.models import StorePointModel


class StorePointModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = StorePointModel
        exclude = ["modified_by", "created_by"]