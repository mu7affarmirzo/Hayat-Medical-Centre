from django import forms

from apps.account.models import PatientModel, NurseAccountModel
from apps.logus.models import BookingModel
from apps.sanatorium.models import IllnessHistory, InitialAppointmentWithDoctorModel, BasePillsInjectionsModel, \
    BaseProcedureServiceModel, BaseLabResearchServiceModel, FinalAppointmentWithDoctorModel, \
    ConsultingWithCardiologistModel, ConsultingWithNeurologistModel, AppointmentWithOnDutyDoctorOnArrivalModel, \
    RepeatedAppointmentWithDoctorModel, AppointmentWithOnDutyDoctorModel, EkgAppointmentModel, LabResult
from apps.warehouse.models import ChequeItemsModel


class PatientUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'],
        required=False  # Make it optional in case it's empty or not filled
    )

    class Meta:
        model = PatientModel
        fields = [
            'f_name',
            'mid_name',
            'l_name',
            'email',
            'date_of_birth',
            'home_phone_number',
            'mobile_phone_number',
            'address',
            'gender',
        ]


class IllnessHistoryUpdateForm(forms.ModelForm):
    class Meta:
        model = IllnessHistory
        fields = [
            'series_number',
            'type',
            'nurse',
            'doctor'
        ]


class BookingModelUpdateForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y'],
        required=False  # Make it optional in case it's empty or not filled
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y'],
        required=False  # Make it optional in case it's empty or not filled
    )

    class Meta:
        model = BookingModel
        fields = [
            'current_tariff',
            'current_room',
            'current_room_type',
            'start_date',
            'end_date'
        ]


class InitialAppointmentShortForm(forms.ModelForm):
    class Meta:
        model = InitialAppointmentWithDoctorModel
        fields = [
            'complaint',
            'anamnesis_morbi',
            'anamnesis_vitae',
            'diagnosis',
            'cito',
            'summary',
        ]


class FinalAppointmentShortForm(forms.ModelForm):
    class Meta:
        model = FinalAppointmentWithDoctorModel
        fields = [
            'objective_status',
            'height',
            'weight',
            'heart_beat',
            'arterial_high_low',
            'imt',
            'imt_interpretation',
            'file',
            'summary',
            'treatment_results',
        ]


class ConsultingWithCardiologistShortForm(forms.ModelForm):
    class Meta:
        model = ConsultingWithCardiologistModel
        fields = [
            'state',
            'has_cardio_complaints',
            'has_nerve_complaints',
            'other_complaints',
            'history_of_illness',
            'inheritance',
            'height',
            'weight',
            'pulse_general',
            'arterial_high_low',
            'imt',
            'imt_interpretation',
            'file',
            'summary',
            'cito',
            'recommendation',
        ]


class ConsultingWithNeurologistShortForm(forms.ModelForm):
    class Meta:
        model = ConsultingWithNeurologistModel
        fields = [
            'state',
            'is_familiar_with_anamnesis',
            'complaint',
            'anamnesis',
            'cito',
            'summary',
            'recommendation',
        ]


class AppointmentWithOnDutyDoctorOnArrivalShortForm(forms.ModelForm):
    class Meta:
        model = AppointmentWithOnDutyDoctorOnArrivalModel
        fields = [
            'state',
            'complaints',
            'objective_data',
            'temperature',
            'arterial_high_low',
            'pulse',
            'diet',
            'regime',
        ]


class RepeatedAppointmentWithDoctorShortForm(forms.ModelForm):
    class Meta:
        model = RepeatedAppointmentWithDoctorModel
        fields = [
            'state',
            'complaint',
            'objective_data',
            'arterial_high_low',
            'imt',
            'diagnosis',
            'cito',
            'summary',
        ]


class AppointmentWithOnDutyDoctorForm(forms.ModelForm):
    class Meta:
        model = AppointmentWithOnDutyDoctorModel
        fields = [
            'state',
            'complaints',
            'objective_data',
            'arterial_high_low',
            'imt',
            'cito',
            'diagnosis',
            'for_sanatorium_treatment',
            'summary',
        ]

class EkgAppointmentShortForm(forms.ModelForm):
    class Meta:
        model = EkgAppointmentModel
        fields = [
            'state',
            'cito',
            'diagnosis',
            'for_sanatorium_treatment',
            'objective_data',
            'summary',
        ]

class BaseProcedureServiceForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y'],
        required=False  # Make it optional in case it's empty or not filled
    )

    class Meta:
        model = BaseProcedureServiceModel
        fields = [
            'medical_service',
            'quantity',
            'start_date',
            'comments',
        ]


class BasePillsInjectionsForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y'],
        required=False  # Make it optional in case it's empty or not filled
    )

    class Meta:
        model = ChequeItemsModel
        fields = [
            'item',
            'quantity_per_session',
            'period_days',
            'start_date',
            'frequency',
            'comments',
            'instruction',
        ]


class BaseLabResearchServiceForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y'],
        required=False  # Make it optional in case it's empty or not filled
    )

    class Meta:
        model = BaseLabResearchServiceModel
        fields = [
            'lab',
            'start_date',
            'comments',
        ]


class LabResultForm(forms.ModelForm):

    class Meta:
        model = LabResult
        fields = [
            'attached_file',
            'comments',
        ]
