from rest_framework import serializers
from apps.cashbox.models import ReceiptModel


class ReceiptSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReceiptModel
        fields = '__all__'