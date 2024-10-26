from django import forms

from apps.sanatorium.models import ProcedureDaysModel


class ProcedureDaysStatusForm(forms.ModelForm):
    class Meta:
        fields = ['state']
        model = ProcedureDaysModel

