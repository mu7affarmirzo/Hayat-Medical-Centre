from rest_framework import serializers
from typing import List

from apps.account.models import PatientModel, EMCDocumentModel, AppointmentsModel


class PatientModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientModel
        exclude = ["modified_by", "created_by"]


class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientModel
        fields = '__all__'
        # fields = ['f_name',
        #           'mid_name',
        #           'l_name',
        #           'home_phone_number',
        #           'mobile_phone_number',
        #           'address',
        #           'INN',
        #           'country',
        #           'date_of_birth',
        #
        #         ]


class PatientSearchSerializer(serializers.Serializer):
    f_name = serializers.CharField(max_length=255, allow_null=True)
    mid_name = serializers.CharField(max_length=255, allow_null=True)
    l_name = serializers.CharField(max_length=255, allow_null=True)
    inn = serializers.CharField(max_length=255, allow_null=True)
    doc_number = serializers.IntegerField(allow_null=True)
    date_of_birth = serializers.DateTimeField(allow_null=True)
    mobile_phone_number = serializers.IntegerField(allow_null=True)
    id = serializers.IntegerField(allow_null=True)
    last_visit_at = serializers.DateTimeField(allow_null=True)

    class Meta:
        fields = '__all__'


class PatientsMergeSerializer(serializers.Serializer):
    class PatientsMergeItemSerializer(serializers.Serializer):
        id = serializers.IntegerField(allow_null=False)
        is_base = serializers.BooleanField(allow_null=False)
        class Meta:
            fields = '__all__'

    patients = PatientsMergeItemSerializer(many=True)

    def save(self, **kwargs):
        # TODO: update Merging Logic after LIS implementation
        target_patient_profile: PatientModel
        source_patient_profiles: List[PatientModel] = []
        for patient in self.validated_data["patients"]:
            patient = dict(patient)
            if patient.get("is_base"):
                target_patient_profile = PatientModel.objects.get(pk=patient.get("id"))
            else:
                source_patient_profiles.append(PatientModel.objects.get(pk=patient.get("id")))

        for source_patient_profile in  source_patient_profiles:

            source_emc = EMCDocumentModel.objects.filter(patient=source_patient_profile).first()
            if source_emc is not None:
                source_emc.patient = target_patient_profile
                source_emc.save(update_fields=['patient'])

            source_appointment = AppointmentsModel.objects.filter(patient=source_patient_profile).first()
            if source_appointment is not None:
                source_appointment.patient = target_patient_profile
                source_appointment.save(update_fields=['patient'])

            source_patient_profile.delete()
    class Meta:
        fields = '__all__'

