from rest_framework import serializers
from apps.warehouse.models import SendRegistryModel


class SendRegistryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = SendRegistryModel
        exclude = ["modified_by", "created_by"]