from django import forms
from django.forms import inlineformset_factory

from apps.warehouse.models import IncomeModel, IncomeItemsModel, StorePointStaffModel, ItemsInStockModel


class IncomeForm(forms.ModelForm):

    class Meta:
        model = IncomeModel
        fields = '__all__'
        exclude = ['created_by', 'modified_by']
        widgets = {
            'serial': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'delivery_company': forms.Select(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'receiver': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'state': forms.Select(
                attrs={
                    'class': 'form-control',
                    'readonly': 'readonly'
                }
            ),
            'bill_amount': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                },

            ),
        }


class VariantForm(forms.ModelForm):

    class Meta:
        model = IncomeItemsModel
        fields = [
            'item', 'price', 'quantity', 'expire_date'
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
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'expire_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            )
        }


VariantFormSet = inlineformset_factory(
    IncomeModel, IncomeItemsModel, form=VariantForm,
    extra=1, can_delete=True, can_delete_extra=True
)

