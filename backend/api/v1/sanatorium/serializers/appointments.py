from rest_framework import serializers
from apps.sanatorium.models import (
    RepeatedAppointmentWithDoctorModel,
    BasePillsInjectionsModel,
    BaseLabResearchServiceModel, BaseMedicalServiceModel, BaseProcedureServiceModel, FinalAppointmentWithDoctorModel,
    DiagnosisTemplate
)


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
        medical_services = validated_data.pop('medical_services')
        lab_research = validated_data.pop('lab_research')
        procedures = validated_data.pop('procedures')
        pills = validated_data.pop('pills')

        rep_appointment = RepeatedAppointmentWithDoctorModel(**validated_data)
        rep_appointment.save()

        for med_serv in medical_services:
            BaseMedicalServiceModel.objects.create(
                model_type='repeated_app',
                model_ref_id=rep_appointment.id,
                illness_history=rep_appointment.illness_history,
                created_by=rep_appointment.created_by,
                **med_serv
            )
            for proc in procedures:
                BaseProcedureServiceModel.objects.create(
                    model_type='repeated_app',
                    model_ref_id=rep_appointment.id,
                    illness_history=rep_appointment.illness_history,
                    created_by=rep_appointment.created_by,
                    **proc
                )

            for l in lab_research:
                BaseLabResearchServiceModel.objects.create(
                    model_type='repeated_app',
                    model_ref_id=rep_appointment.id,
                    illness_history=rep_appointment.illness_history,
                    created_by=rep_appointment.created_by,
                    **l
                )

            for pill in pills:
                BasePillsInjectionsModel.objects.create(
                    model_type='repeated_app',
                    model_ref_id=rep_appointment.id,
                    illness_history=rep_appointment.illness_history,
                    created_by=rep_appointment.created_by,
                    **pill
                )

        return rep_appointment


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
        fields = '__all__'
        model = FinalAppointmentWithDoctorModel
