from rest_framework import serializers
from apps.warehouse.models import SentItemsModel


class SentItemsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = SentItemsModel
        fields = "__all__"