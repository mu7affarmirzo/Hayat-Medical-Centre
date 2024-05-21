# serializers.py
from rest_framework import serializers

from api.v1.organizations.serializers import PatientModelSerializer
from apps.lis.models import OrderedLabResearchModel, TestResultModel
from apps.lis.models.lab_researchs import LabResearchCategoryModel, LabResearchModel, LabResearchSubCategoryModel, \
    LabResearchTestModel


class LabResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabResearchModel
        fields = '__all__'


class LabResearchCategorySerializer(serializers.ModelSerializer):
    lab_research = LabResearchSerializer(many=True, read_only=True)

    class Meta:
        model = LabResearchCategoryModel
        fields = [
            'id',
            'name',
            'lab_research'
        ]


class ListSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LabResearchSubCategoryModel
        fields = '__all__'


class ListCategorySerializer(serializers.ModelSerializer):
    sub_categories = ListSubCategorySerializer(many=True)

    class Meta:
        model = LabResearchCategoryModel
        fields = '__all__'


class ListLabResearchTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabResearchTestModel
        fields = [
            'name',
            'number',
            'measurement_unit',
            'is_active',
        ]


class ListLabResearchSerializer(serializers.ModelSerializer):
    lab_research_test = ListLabResearchTestSerializer(many=True)

    class Meta:
        model = LabResearchModel
        fields = [
            'name',
            'number',
            'branch',
            'is_active',
            'lab_research_test'
        ]


class TestResultModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResultModel
        fields = "__all__"


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
