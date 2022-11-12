from rest_framework import serializers
from apps.account.models import Account, DoctorSpecialityModel


class DoctorsCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = "__all__"

    extra_kwargs = {
        'password': {'write_only': True}
    }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            phone_number=self.validated_data['phone_number'],
            f_name=self.validated_data['f_name'],
            l_name=self.validated_data['l_name'],
            m_name=self.validated_data['m_name'],
            sex=self.validated_data['sex'],
            organization_id=self.validated_data['organization_id'],
            branch_id=self.validated_data['branch_id'],
            color=self.validated_data['color'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match!'})
        account.set_password(password)
        account.save()
        return account


class DoctorsListSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = [
            'id',
            'email',
            'username',
            'f_name',
            'l_name',
            'm_name',
            'phone_number',
            'sex',
            'organization_id',
            'branch_id',
            'color',
            'created_by'
        ]

    def get_created_by(self, account):
        target_doctor = DoctorSpecialityModel.objects.filter(doctor=account)[0]
        created_by = target_doctor.created_by.email
        return created_by


