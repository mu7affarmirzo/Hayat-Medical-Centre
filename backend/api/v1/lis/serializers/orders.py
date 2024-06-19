from rest_framework import serializers

from api.v1.lis.serializers.labs import TestResultModelSerializer
from api.v1.organizations.serializers import PatientModelSerializer
from apps.lis.models import OrderedLabResearchModel, TestResultModel


class OrderedLabResearchSerializer(serializers.ModelSerializer):
    patient = PatientModelSerializer()
    results = serializers.SerializerMethodField("get_test_results")

    class Meta:
        model = OrderedLabResearchModel
        fields = [
            'patient',
            'created_at',
            'order_number',
            'lab',
            'branch_name',
            'results'
        ]

    def get_test_results(self, obj: OrderedLabResearchModel):
        test_results = TestResultModel.objects.filter(ordered_lab_research=obj)
        serializer = TestResultModelSerializer(test_results, many=True)
        return serializer.data


class OrderedLabResearchFilterSerializer(serializers.Serializer):
    start = serializers.DateField(required=False)
    end = serializers.DateField(required=False)
    branch = serializers.CharField(required=False)
    barcode = serializers.CharField(required=False)
    lab = serializers.CharField(required=False)
    container = serializers.CharField(required=False)
    category = serializers.CharField(required=False)
    patient = serializers.CharField(required=False)
    order_status = serializers.ChoiceField(required=False, choices=OrderedLabResearchModel.OrderStatus.choices)
    date_birth = serializers.DateField(required=False)
    container_connected = serializers.BooleanField(required=False)


class UpdateContainerCodeSerializer(serializers.Serializer):
    container_code = serializers.CharField()
    container_id = serializers.IntegerField(required=False)


class ValidateStatusesSerializer(serializers.Serializer):
    choice = serializers.ChoiceField(choices=OrderedLabResearchModel.ValidateStatus.choices)
