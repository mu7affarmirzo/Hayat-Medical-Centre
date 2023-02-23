from rest_framework import serializers
from apps.warehouse.models import ReceivedItemsModel


class ReceivedItemsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReceivedItemsModel
        exclude = ["modified_by", "created_by"]