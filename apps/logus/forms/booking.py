from django import forms

from apps.account.models import PatientModel
from apps.logus.models import BookingModel
from apps.sanatorium.models import IllnessHistory


class BookingForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']
    )

    is_sick_leave = forms.BooleanField(
        required=False,
        label="Больничный"
    )

    class Meta:
        model = BookingModel
        fields = [
            'current_tariff', 'current_room',
            'current_room_type', 'patient',
            'start_date', 'end_date',
        ]
        # widgets = {
        #     'start_date': forms.DateInput(attrs={'type': 'date'}),
        #     'end_date': forms.DateInput(attrs={'type': 'date'}),
        # }


class UpdateBookingForm(forms.ModelForm):
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
            'current_tariff', 'current_room',
            'current_room_type',
            'start_date', 'end_date', 'stage'
        ]


class UpdateIllnessHistoryForm(forms.ModelForm):
    class Meta:
        model = IllnessHistory
        fields = [
            'series_number',
            'type',
            'nurse',
            'doctor'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['series_number'].required = False
        self.fields['type'].required = False
        self.fields['nurse'].required = False
        self.fields['doctor'].required = False


class PatientRegistrationForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']
    )

    class Meta:
        model = PatientModel
        fields = [
            'f_name', 'mid_name', 'l_name', 'address',
            'date_of_birth', 'mobile_phone_number', 'gender', 'INN'
        ]


class AddCompanionForm(forms.ModelForm):
    class Meta:
        model = IllnessHistory
        fields = [
            'type',
            'is_sick_leave',
            'patient',

        ]