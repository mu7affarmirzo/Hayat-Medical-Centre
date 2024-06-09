# forms.py
from django import forms

from apps.warehouse.models import IncomeModel, IncomeItemsModel


class IncomeForm(forms.ModelForm):
    class Meta:
        model = IncomeModel
        fields = ['delivery_company', 'receiver', 'bill_amount', 'created_by']


class IncomeItemsForm(forms.ModelForm):
    class Meta:
        model = IncomeItemsModel
        fields = ['item', 'price', 'quantity']


IncomeItemsFormSet = forms.inlineformset_factory(IncomeModel, IncomeItemsModel, form=IncomeItemsForm, extra=1)
