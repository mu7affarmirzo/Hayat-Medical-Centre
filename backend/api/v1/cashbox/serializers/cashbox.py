from rest_framework import serializers

from api.v1.organizations.serializers import DoctorAccountListSerializer
from apps.account.models import BranchModel
from apps.cashbox.models import CashBoxClosingHistoryRecordsModel

TYPE_CHOICES =(
    ("OUTCOME", "OUTCOME"),
    ("INCOME", "INCOME"),

)


class BranchModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = BranchModel
        fields = '__all__'


class CashBoxSerializer(serializers.ModelSerializer):
    created_by = DoctorAccountListSerializer()
    branch = BranchModelSerializer()

    class Meta:
        model = CashBoxClosingHistoryRecordsModel
        fields = '__all__'


class TypeSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=TYPE_CHOICES)

    class Meta:
        fields = '__all__'