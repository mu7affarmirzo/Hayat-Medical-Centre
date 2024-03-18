# serializers.py
from rest_framework import serializers

from apps.lis.models.lab_researchs import LabResearchCategoryModel, LabResearchModel


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
