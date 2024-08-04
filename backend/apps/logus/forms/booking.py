from django import forms

from apps.account.models import PatientModel
from apps.logus.models import BookingModel


class BookingForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']
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


class PatientRegistrationForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']
    )

    class Meta:
        model = PatientModel
        fields = [
            'f_name', 'mid_name', 'l_name',
            'date_of_birth', 'mobile_phone_number', 'gender'
        ]
