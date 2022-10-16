from rest_framework import serializers
from account.models.accounts import Account
from account.models.roles_permissions import AccountRolesModel, RolesModel


class DoctorsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = "__all__"


class DoctorsListSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = '__all__'

    def get_created_by(self, organization):
        created_by = organization.created_by.username
        return created_by


