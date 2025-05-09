from django import forms
from django.forms import inlineformset_factory

from apps.warehouse.models import ExpenseItemsModel, ExpenseModel, StorePointStaffModel, ItemsInStockModel


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
            'item', 'quantity',
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
        }

    def __init__(self, *args, **kwargs):
        # Get additional parameters if provided
        user = kwargs.pop('user', None)
        store_point = StorePointStaffModel.objects.filter(staff=user)

        store_point = store_point.first()
        warehouse = store_point.store_point
        super().__init__(*args, **kwargs)
        self.fields['item'].queryset = ItemsInStockModel.objects.filter(warehouse=warehouse)


VariantFormSet = inlineformset_factory(
    ExpenseModel, ExpenseItemsModel, form=VariantForm,
    extra=1, can_delete=True, can_delete_extra=True
)
