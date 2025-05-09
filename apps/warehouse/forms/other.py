from django import forms
from django.contrib.auth import authenticate

from apps.account.models import Account
from apps.warehouse.models import ItemsModel, IncomeModel, IncomeItemsModel


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid inputs")


class ItemSearchForm(forms.Form):
    search = forms.CharField(label="search")


class AddItemToChequeForm(forms.Form):
    itemid = forms.IntegerField()
    quantity = forms.IntegerField()


class AddItemForm(forms.Form):
    is_medicine = forms.CheckboxInput()
    item_name = forms.CharField()
    trade_name = forms.CharField()
    dosage = forms.CharField()
    fvip = forms.CharField()
    number = forms.CharField()
    company = forms.CharField()
    unit = forms.CharField()


class ItemForm(forms.ModelForm):
    created_by = forms.ModelChoiceField(queryset=Account.objects.all(), label='Пользователь')

    class Meta:
        model = ItemsModel
        fields = ['name', 'company', 'in_pack', 'seria']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'seria': forms.TextInput(attrs={'class': 'form-control'}),
            'in_pack': forms.NumberInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
        }


class IncomeForm(forms.ModelForm):
    class Meta:
        model = IncomeModel
        fields = (
            'serial', 'delivery_company', 'receiver', 'bill_amount',
        )


class IncomeItemsForm(forms.ModelForm):
    class Meta:
        model = IncomeItemsModel
        fields = ['item', "price", 'quantity']


# Formset for handling multiple items
IncomeItemsFormSet = forms.inlineformset_factory(
    IncomeModel, IncomeItemsModel,
    form=IncomeItemsForm, extra=1
)

