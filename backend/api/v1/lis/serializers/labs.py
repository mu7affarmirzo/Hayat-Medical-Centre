# serializers.py
from rest_framework import serializers

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

