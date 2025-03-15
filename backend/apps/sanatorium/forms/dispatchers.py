from datetime import datetime

from django import forms

from apps.sanatorium.models import BaseProcedureServiceModel, ProcedureDaysModel


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


from django import forms
from datetime import datetime

class ProcedureDaysModelForm(forms.ModelForm):

    class Meta:
        model = ProcedureDaysModel
        fields = [
            'state',
            'start_at',
            'procedure_doctor',
            'comments',
        ]

    def clean_start_at(self):
        start_at = self.cleaned_data.get('start_at')
        return datetime.strptime(start_at, '%m/%d/%Y %I:%M %p')
        # try:
        #     # Adjust the format here to match the incoming date format.
        #     return datetime.strptime(start_at, '%m/%d/%Y %I:%M %p')
        # except (ValueError, TypeError):
        #     raise forms.ValidationError('Введите правильную дату и время.')
