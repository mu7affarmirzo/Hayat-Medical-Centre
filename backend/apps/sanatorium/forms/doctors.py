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


from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput, CheckboxInput


class InitialAppointmentWithDoctorForm(ModelForm):
    class Meta:
        model = InitialAppointmentWithDoctorModel
        exclude = ['created_by', 'created_at', 'modified_at', 'modified_by', 'doctor', 'illness_history', 'state']

        widgets = {
            # Anamnesis
            'complaint': Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': ' ...'}),
            'anamnesis_morbi': Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '...'}),
            'anamnesis_vitae': Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '...'}),

            # Epidanamnesis
            'contact_with_infectious': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'на протяжении максимального срока инкубации: не было'}),
            'contact_with_orvi': CheckboxInput(attrs={'class': 'custom-control-input'}),
            'is_away_two_month': CheckboxInput(attrs={'class': 'custom-control-input'}),
            'transferred_infectious': TextInput(attrs={'class': 'form-control', 'placeholder': 'нет'}),
            'staying_hospital': TextInput(attrs={'class': 'form-control', 'placeholder': 'нет'}),
            'receiving_blood_transfusions': TextInput(attrs={'class': 'form-control', 'placeholder': 'нет'}),
            'surgical_massive_interventions_six_months': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'нет'}),
            'dentist_visits_last_six_months': TextInput(attrs={'class': 'form-control', 'placeholder': 'нет'}),
            'profession_toxics': TextInput(attrs={'class': 'form-control'}),
            'additional_data': TextInput(attrs={'class': 'form-control'}),

            # Status praesens objectivus
            'general_state': TextInput(attrs={'class': 'form-control'}),
            'consciousness': Select(attrs={'class': 'form-control'}),
            'consciousness_state': Select(attrs={'class': 'form-control'}),
            'constitution': Select(attrs={'class': 'form-control'}),
            'skin': Select(attrs={'class': 'form-control'}),
            'pigmentation': TextInput(attrs={'class': 'form-control'}),
            'depigmentation': TextInput(attrs={'class': 'form-control'}),
            'rashes': TextInput(attrs={'class': 'form-control'}),
            'vascular_changes': TextInput(attrs={'class': 'form-control'}),
            'hemorrhages': TextInput(attrs={'class': 'form-control'}),
            'scarring': TextInput(attrs={'class': 'form-control'}),
            'trophic_changes': TextInput(attrs={'class': 'form-control'}),
            'visible_tumors': TextInput(attrs={'class': 'form-control'}),
            'skin_moisture': Select(attrs={'class': 'form-control'}),
            'skin_turgor': Select(attrs={'class': 'form-control'}),
            'subcutaneous_fat': Select(attrs={'class': 'form-control'}),

            # Physical parameters
            'temperature': NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'height': NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'weight': NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'heart_beat': NumberInput(attrs={'class': 'form-control'}),
            'arterial_high': NumberInput(attrs={'class': 'form-control'}),
            'arterial_low': NumberInput(attrs={'class': 'form-control'}),
            'imt': NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'extra_weight': NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'swelling_pastiness': TextInput(attrs={'class': 'form-control'}),
            'lymph_nodes': Select(attrs={'class': 'form-control'}),

            # Bone-muscular system
            'deformations': TextInput(attrs={'class': 'form-control'}),
            'contractures': TextInput(attrs={'class': 'form-control'}),
            'movement_restrictions': TextInput(attrs={'class': 'form-control'}),

            # Respiratory system
            'respiratory_frequency': NumberInput(attrs={'class': 'form-control'}),
            'breathing_type': Select(attrs={'class': 'form-control'}),
            'auscultative_breathing': Select(attrs={'class': 'form-control'}),
            'wheezing': Select(attrs={'class': 'form-control'}),
            'coughing': Select(attrs={'class': 'form-control'}),
            'high_humidity': TextInput(attrs={'class': 'form-control'}),
            'crepitus': Select(attrs={'class': 'form-control'}),
            'lungs_percussion': Select(attrs={'class': 'form-control'}),

            # Cardiovascular system
            'heart_edge': Select(attrs={'class': 'form-control'}),
            'heart_tones': Select(attrs={'class': 'form-control'}),
            'accent_in_aorta': Select(attrs={'class': 'form-control'}),
            'noise_change_on_ot': Select(attrs={'class': 'form-control'}),
            'ad_left': TextInput(attrs={'class': 'form-control'}),
            'ad_right': TextInput(attrs={'class': 'form-control'}),
            'ps_left': TextInput(attrs={'class': 'form-control'}),
            'ps_right': TextInput(attrs={'class': 'form-control'}),
            'pulse_noise_on_arteria': Select(attrs={'class': 'form-control'}),

            # Digestive system
            'appetit': Select(attrs={'class': 'form-control'}),
            'tongue': Select(attrs={'class': 'form-control'}),
            'cracks_ulcers_in_mouth': Select(attrs={'class': 'form-control'}),
            'stomach': Select(attrs={'class': 'form-control'}),
            'liver': Select(attrs={'class': 'form-control'}),
            'liver_edge': Select(attrs={'class': 'form-control'}),
            'spleen': Select(attrs={'class': 'form-control'}),
            'spleen_edge': Select(attrs={'class': 'form-control'}),
            'stool': Select(attrs={'class': 'form-control'}),
            'stool_frequency': TextInput(attrs={'class': 'form-control'}),

            # Urinary system
            'urinary_system': TextInput(attrs={'class': 'form-control'}),
            'effleurage_symptoms': Select(attrs={'class': 'form-control'}),

            # Other systems
            'thyroid': Select(attrs={'class': 'form-control'}),
            'nerve_system': Select(attrs={'class': 'form-control'}),

            # Diagnosis and summary
            'diagnosis': Select(attrs={'class': 'form-control select2', 'style': 'width: 100%;'}),
            'cito': CheckboxInput(attrs={'class': 'custom-control-input'}),
            'summary': Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Резюме...'}),
        }

    def __init__(self, *args, **kwargs):
        super(InitialAppointmentWithDoctorForm, self).__init__(*args, **kwargs)

        # Set default values
        if not self.instance.pk:  # If this is a new instance (not editing existing)
            self.fields['contact_with_infectious'].initial = 'на протяжении максимального срока инкубации: не было'
            self.fields['temperature'].initial = 36.6
            self.fields['auscultative_breathing'].initial = 'везикулярное'
            self.fields['wheezing'].initial = 'влажное'
            self.fields['lungs_percussion'].initial = 'ясный'
            self.fields['heart_edge'].initial = 'расширены'
            self.fields['heart_tones'].initial = 'звучанные'
            self.fields['ad_left'].initial = '130/80'
            self.fields['ad_right'].initial = '130/80'
            self.fields['ps_left'].initial = '75'
            self.fields['ps_right'].initial = '75'
            self.fields['pulse_noise_on_arteria'].initial = 'сонная'
            self.fields['appetit'].initial = 'удовлетворительный'
            self.fields['tongue'].initial = 'чистый, влажный'
            self.fields['stomach'].initial = 'мягкий'
            self.fields['liver'].initial = 'не увеличени'
            self.fields['spleen'].initial = 'не увеличени'
            self.fields['stool'].initial = 'запоры'
            self.fields['stool_frequency'].initial = '1'
            self.fields['urinary_system'].initial = '1'
            self.fields['effleurage_symptoms'].initial = 'отрицательный'
            self.fields['thyroid'].initial = 'без изменений'
            self.fields['nerve_system'].initial = 'без изменений'



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
