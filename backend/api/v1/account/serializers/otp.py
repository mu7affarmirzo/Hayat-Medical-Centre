from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from apps.account.models import Account
from apps.account.models.otp import OtpModel


class OtpSerializer(serializers.ModelSerializer):

    class Meta:
        model = OtpModel
        fields = ['email']


class StepTwoSerializer(serializers.Serializer):
    otp_token = serializers.CharField(max_length=255)
    otp = serializers.CharField(max_length=255)

    class Meta:
        fields = '__all__'


class ForgotPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ('password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance