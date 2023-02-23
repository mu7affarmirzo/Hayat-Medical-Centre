from rest_framework import serializers
from apps.warehouse.models import ReceiveRegistryModel


class ReceiveRegistryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReceiveRegistryModel
        exclude = ["modified_by", "created_by"]