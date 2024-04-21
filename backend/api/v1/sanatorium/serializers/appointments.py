from rest_framework import serializers
from apps.sanatorium.models import (
    RepeatedAppointmentWithDoctorModel,
    BasePillsInjectionsModel,
    BaseLabResearchServiceModel, BaseMedicalServiceModel, BaseProcedureServiceModel, FinalAppointmentWithDoctorModel,
    DiagnosisTemplate, ConsultingWithNeurologistModel, ConsultingWithCardiologistModel,
    AppointmentWithOnDutyDoctorModel,
    AppointmentWithOnDutyDoctorOnArrivalModel, EkgAppointmentModel
)


def create(validated_data, target_model, model_type: str):
    medical_services = validated_data.pop('medical_services')
    lab_research = validated_data.pop('lab_research')
    procedures = validated_data.pop('procedures')
    pills = validated_data.pop('pills')

    target = target_model(**validated_data)
    target.save()

    for med_serv in medical_services:
        BaseMedicalServiceModel.objects.create(
            model_type=model_type,
            model_ref_id=target.id,
            illness_history=target.illness_history,
            created_by=target.created_by,
            **med_serv
        )
        for proc in procedures:
            BaseProcedureServiceModel.objects.create(
                model_type=model_type,
                model_ref_id=target.id,
                illness_history=target.illness_history,
                created_by=target.created_by,
                **proc
            )

        for l in lab_research:
            BaseLabResearchServiceModel.objects.create(
                model_type=model_type,
                model_ref_id=target.id,
                illness_history=target.illness_history,
                created_by=target.created_by,
                **l
            )

        for pill in pills:
            BasePillsInjectionsModel.objects.create(
                model_type=model_type,
                model_ref_id=target.id,
                illness_history=target.illness_history,
                created_by=target.created_by,
                **pill
            )

    return target


class BaseMedicalServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseMedicalServiceModel
        fields = [
            'medical_service',
            'consulted_doctor',
            'state',
        ]


class BaseProceduresSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProcedureServiceModel
        fields = [
            'medical_service',
            'quantity',
            'start_date',
            'frequency',
            'comments',
        ]


class BaseLabResearchServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseLabResearchServiceModel
        fields = [
            'lab',
            'start_date',
            'comments',
        ]


class BasePPillsInjectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasePillsInjectionsModel
        fields = [
            'pills_injections',
            'state',
            'quantity',
            'period_days',
            'start_date',
            'end_date',
            'frequency',
            'comments',
            'instruction'
        ]


class RepeatedAppointmentSerializer(serializers.ModelSerializer):
    medical_services = BaseMedicalServicesSerializer(many=True)
    lab_research = BaseLabResearchServiceSerializer(many=True)
    procedures = BaseProceduresSerializer(many=True)
    pills = BasePPillsInjectionsSerializer(many=True)

    class Meta:
        model = RepeatedAppointmentWithDoctorModel
        fields = '__all__'
        read_only = ['created_at', 'updated_at', 'doctor', 'created_by', 'updated_by']

    def create(self, validated_data):
        result = create(validated_data, RepeatedAppointmentWithDoctorModel, 'repeated_app')
        return result


class FinalAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = FinalAppointmentWithDoctorModel
        read_only = [
            'created_by',
            'created_at',
            'modified_at',
            'modified_by',
            'state'
        ]


class DiagnosisTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisTemplate
        fields = '__all__'


class FinalAppointmentDetailedSerializer(serializers.ModelSerializer):
    diagnosis = DiagnosisTemplateSerializer(many=True)

    class Meta:
        model = FinalAppointmentWithDoctorModel
        fields = '__all__'
        read_only = [
            'created_by',
            'created_at',
            'modified_at',
            'modified_by',
        ]


class ConsultingWithNeurologistSerializer(serializers.ModelSerializer):
    medical_services = BaseMedicalServicesSerializer(many=True)
    lab_research = BaseLabResearchServiceSerializer(many=True)
    procedures = BaseProceduresSerializer(many=True)
    pills = BasePPillsInjectionsSerializer(many=True)

    class Meta:
        model = ConsultingWithNeurologistModel
        fields = '__all__'
        read_only = [
            'created_by',
            'created_at',
            'modified_at',
            'modified_by',
        ]

    def create(self, validated_data):
        result = create(validated_data, ConsultingWithNeurologistModel, 'neurologist')
        return result


class ConsultingWithCardiologistSerializer(serializers.ModelSerializer):
    medical_services = BaseMedicalServicesSerializer(many=True)
    lab_research = BaseLabResearchServiceSerializer(many=True)
    procedures = BaseProceduresSerializer(many=True)
    pills = BasePPillsInjectionsSerializer(many=True)

    class Meta:
        model = ConsultingWithCardiologistModel
        fields = '__all__'
        read_only = [
            'created_by',
            'created_at',
            'modified_at',
            'modified_by',
        ]

    def create(self, validated_data):
        result = create(validated_data, ConsultingWithCardiologistModel, 'cardiologist')
        return result


class AppointmentWithOnDutyDoctorSerializer(serializers.ModelSerializer):
    medical_services = BaseMedicalServicesSerializer(many=True)
    lab_research = BaseLabResearchServiceSerializer(many=True)
    procedures = BaseProceduresSerializer(many=True)
    pills = BasePPillsInjectionsSerializer(many=True)

    class Meta:
        model = AppointmentWithOnDutyDoctorModel
        fields = '__all__'
        read_only = [
            'created_by',
            'created_at',
            'modified_at',
            'modified_by',
            'doctor'
        ]

    def create(self, validated_data):
        result = create(validated_data, AppointmentWithOnDutyDoctorModel, 'on_duty_doctor')
        return result


class AppointmentWithOnDutyDoctorOnArrivalSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppointmentWithOnDutyDoctorOnArrivalModel
        fields = '__all__'
        read_only = [
            'created_by',
            'created_at',
            'modified_at',
            'modified_by',
            'doctor'
        ]


class EkgAppointmentSerializer(serializers.ModelSerializer):
    medical_services = BaseMedicalServicesSerializer(many=True)
    lab_research = BaseLabResearchServiceSerializer(many=True)
    procedures = BaseProceduresSerializer(many=True)
    pills = BasePPillsInjectionsSerializer(many=True)

    class Meta:
        model = EkgAppointmentModel
        fields = '__all__'

        read_only = [
            'created_by',
            'created_at',
            'modified_at',
            'modified_by',
            'doctor'
        ]

    def create(self, validated_data):
        result = create(validated_data, EkgAppointmentModel, 'ekg')
        return result

