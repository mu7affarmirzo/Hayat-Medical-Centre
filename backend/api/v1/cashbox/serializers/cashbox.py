from rest_framework import serializers
from apps.cashbox.models import CashBoxClosingHistoryRecordsModel

TYPE_CHOICES =(
    ("OUTCOME", "OUTCOME"),
    ("INCOME", "INCOME"),

)

class CashBoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = CashBoxClosingHistoryRecordsModel
        fields = '__all__'

class TypeSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=TYPE_CHOICES)

    class Meta:
        fields = '__all__'