from django import forms

from apps.warehouse.models import ItemsModel, CompanyModel


class ItemsModelCreateForm(forms.ModelForm):

    class Meta:
        model = ItemsModel
        fields = [
            'company',
            'in_pack',
            'name',
            'unit',
            'seria',
        ]

