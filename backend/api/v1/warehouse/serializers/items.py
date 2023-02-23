from rest_framework import serializers

from apps.warehouse.models import ItemsModel


class ItemsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsModel
        fields = "__all__"