from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        token['organization'] = user.organization_id
        token['branch'] = user.branch_id
        a = [x for x in user.account_role_user.all()]
        roles = dict()
        for i in a:
            temp = 0
            roles[temp] = i.role.name
            temp += 1
        token['user_role'] = roles
        return token
