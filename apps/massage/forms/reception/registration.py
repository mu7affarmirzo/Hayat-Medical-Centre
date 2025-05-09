from django import forms

from apps.massage.models import PatientModel, SessionModel


class SessionForm(forms.ModelForm):
    # start_date = forms.DateTimeField(
    #     widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
    #     input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']
    # )

    class Meta:
        model = SessionModel
        fields = [
            # 'start_date',
            'patient',
            'massage',
            'therapist',
            'quantity',
            'discount',
        ]


class PatientRegistrationForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']
    )

    class Meta:
        model = PatientModel
        fields = [
            'f_name', 'mid_name', 'l_name', 'address',
            'date_of_birth', 'mobile_phone_number', 'gender',
        ]