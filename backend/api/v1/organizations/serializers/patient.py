from rest_framework import serializers
from account.models.patients import PatientModel


class PatientModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientModel
        fields = '__all__'


class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientModel
        fields = ['f_name',
                  'mid_name',
                  'l_name',
                  'home_phone_number',
                  'mobile_phone_number',
                  'address',
                  'INN',
                  'country',
                ]


class PatientSearchSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255, allow_null=True)
    inn = serializers.CharField(max_length=255, allow_null=True)
    doc_number = serializers.IntegerField(allow_null=True)
    date_of_birth = serializers.DateTimeField(allow_null=True)
    mobile_phone_number = serializers.IntegerField(allow_null=True)
    id = serializers.IntegerField(allow_null=True)
    last_visit_at = serializers.DateTimeField(allow_null=True)

    class Meta:
        fields = '__all__'


