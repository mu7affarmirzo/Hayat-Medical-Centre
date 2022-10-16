from rest_framework import serializers
from account.models.organizations import OrganizationModel, BranchModel


class OrganizationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationModel
        fields = [
            'name',
        ]


class OrganizationListSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = OrganizationModel
        fields = '__all__'

    def get_created_by(self, organization):
        created_by = organization.created_by.username
        return created_by


class BranchCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BranchModel
        fields = [
            'name',
            'organization'
        ]


class BranchListSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    modified_by = serializers.SerializerMethodField()

    class Meta:
        model = BranchModel
        fields = '__all__'

    def get_created_by(self, organization):
        created_by = organization.created_by.username
        return created_by

    def get_modified_by(self, organization):
        modified_by = organization.modified_by.username
        return modified_by
