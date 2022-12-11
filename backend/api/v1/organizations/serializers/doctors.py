from rest_framework import serializers
from apps.account.models import Account, DoctorSpecialityModel, DoctorAccountModel


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

        doctor = DoctorAccountModel(doctor=account)
        doctor.save()
        return account


class DoctorAccountListSerializer(serializers.ModelSerializer):
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
        ]


class DoctorsListSerializer(serializers.ModelSerializer):
    doctor = DoctorAccountListSerializer()
    specialty = serializers.SerializerMethodField()
    is_at_work = serializers.SerializerMethodField()

    class Meta:
        model = DoctorAccountModel
        fields = [
            'id',
            'doctor',
            'specialty',
            'is_at_work'
        ]
        ordering = ('doctor__l_name',)

    def get_specialty(self, obj):
        specialties = {}
        for i in obj.doc_speciality.all():
            specialties[i.speciality.name] = {
                "name": i.speciality.name,
                "id": i.speciality.id,
            }

        return specialties

    def get_is_at_work(self, obj):

        if obj.doctor.attendance.first() is not None:
            return obj.doctor.attendance.first().is_at_work
        else:
            return False


class DoctorSearchSerializer(serializers.Serializer):
    f_name = serializers.CharField(max_length=255, allow_null=True)
    mid_name = serializers.CharField(max_length=255, allow_null=True)
    l_name = serializers.CharField(max_length=255, allow_null=True)
    mobile_phone_number = serializers.IntegerField(allow_null=True)


