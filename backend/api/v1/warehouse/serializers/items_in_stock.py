from rest_framework import serializers
from apps.warehouse.models import ItemsInStockModel


class ItemsInStockModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemsInStockModel
        fields = "__all__"