from django import forms
from django.forms import inlineformset_factory

from apps.warehouse.models import IncomeModel, IncomeItemsModel


class ProductForm(forms.ModelForm):

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
            'item', 'price', 'quantity',
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
        }


VariantFormSet = inlineformset_factory(
    IncomeModel, IncomeItemsModel, form=VariantForm,
    extra=1, can_delete=True, can_delete_extra=True
)
# from django import forms
# from django.forms import inlineformset_factory
#
# from apps.warehouse.models import IncomeModel, IncomeItemsModel
#
#
# class IncomeForm(forms.ModelForm):
#     class Meta:
#         model = IncomeModel
#         fields = ['delivery_company', 'receiver', 'bill_amount', 'created_by']
#
#
# class IncomeItemsForm(forms.ModelForm):
#     class Meta:
#         model = IncomeItemsModel
#         fields = ['item', 'price', 'quantity', 'created_by']
#
#
# IncomeItemsFormSet = inlineformset_factory(
#     IncomeModel, IncomeItemsModel, form=IncomeItemsForm,
#     fields=('item', 'price', 'quantity', 'created_by'), extra=1, can_delete=True
# )
