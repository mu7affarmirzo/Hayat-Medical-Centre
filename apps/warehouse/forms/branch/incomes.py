from django import forms
from django.forms import inlineformset_factory

from apps.warehouse.models import SendRegistryModel, SentItemsModel


class AcceptIncomesForm(forms.ModelForm):

    class Meta:
        model = SendRegistryModel
        fields = ['series', 'receiver', 'state']
        readonly_fields = ['series', 'receiver']
        widgets = {
            'series': forms.TextInput(
                attrs={
                    'class': 'form-control disabled',
                    'readonly': 'readonly'
                    },
                ),

            'receiver': forms.Select(
                attrs={
                    'class': 'form-control',
                    'readonly': 'readonly'

                }
            ),
            'state': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['series'].widget.attrs['disabled'] = True
            self.fields['receiver'].widget.attrs['disabled'] = True


class AcceptVariantForm(forms.ModelForm):

    class Meta:
        model = SentItemsModel
        fields = [
            'item', 'quantity', 'state', 'expire_date'
        ]
        readonly_fields = ['item', 'quantity', 'expire_date']
        widgets = {
            'item': forms.Select(
                attrs={
                    'class': 'form-control',
                    'readonly': 'readonly'
                }
                ),
            'state': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'readonly': 'readonly'
                },
                ),
            'expire_date': forms.DateInput(
                format='%Y-%m-%d',  # Adjust the format as per your model field and locale preferences
                attrs={
                    'class': 'form-control',
                    'type': 'date',  # This makes the browser use the native date picker
                    'readonly': 'readonly'
                }
            ),
        }


AcceptVariantFormSet = inlineformset_factory(
    SendRegistryModel, SentItemsModel, form=AcceptVariantForm,
    extra=1, can_delete=True, can_delete_extra=True
)
