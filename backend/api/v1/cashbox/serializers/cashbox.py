from rest_framework import serializers
from apps.cashbox.models import CashBoxClosingHistoryRecordsModel


class CashBoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = CashBoxClosingHistoryRecordsModel
        fields = '__all__'

