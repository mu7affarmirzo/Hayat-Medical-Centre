from django import forms

from apps.account.models import PatientModel, NurseAccountModel
from apps.logus.models import BookingModel
from apps.sanatorium.models import IllnessHistory


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

    # nurse = forms.SelectMultiple(
    #     choices=NurseAccountModel
    # )


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

