from django import forms
from django.forms import inlineformset_factory

from apps.warehouse.models import ExpenseItemsModel, ExpenseModel


class ExpanseForm(forms.ModelForm):

    class Meta:
        model = ExpenseModel
        fields = ['series', 'receiver']
        widgets = {
            'series': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),

            'receiver': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class VariantForm(forms.ModelForm):

    class Meta:
        model = ExpenseItemsModel
        fields = [
            'item', 'quantity', 'expire_date'
        ]
        widgets = {
            'item': forms.Select(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'expire_date': forms.DateInput(
                format='%Y-%m-%d',  # Adjust the format as per your model field and locale preferences
                attrs={
                    'class': 'form-control',
                    'type': 'date'  # This makes the browser use the native date picker
                }
            ),
        }


VariantFormSet = inlineformset_factory(
    ExpenseModel, ExpenseItemsModel, form=VariantForm,
    extra=1, can_delete=True, can_delete_extra=True
)
