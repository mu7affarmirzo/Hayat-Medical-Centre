from django import forms

from apps.sanatorium.models import BaseProcedureServiceModel


class UpdateBaseProcedureServiceForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y'],
        required=False  # Make it optional in case it's empty or not filled
    )

    class Meta:
        model = BaseProcedureServiceModel
        fields = [
            'procedure_doctor',
            'state',
            'start_date'
        ]


class DispatchBaseProcedureServiceForm(forms.ModelForm):

    class Meta:
        model = BaseProcedureServiceModel
        fields = [
            'procedure_doctor'
        ]