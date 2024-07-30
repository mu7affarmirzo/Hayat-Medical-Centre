from django import forms

from apps.logus.models import TariffModel, AvailableRoomsTypeModel


class DateRangeForm(forms.Form):
    reservation_time = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control float-right',
        'id': 'reservation',
    }))
    tariff = forms.ChoiceField(choices=TariffModel.objects.all(), widget=forms.Select)
    room_type = forms.ChoiceField(choices=AvailableRoomsTypeModel.objects.all())
    # tariff = forms.ModelChoiceField(
    #     queryset=TariffModel.objects.all(),
    #     widget=forms.Select(attrs={'class': 'select_tariff', 'style': 'width: 100%;'})
    # )
    # tariff = forms.ModelChoiceField(queryset=TariffModel.objects.all(), required=False, widget=forms.Select(
    #     attrs={'class': 'select2', 'data-placeholder': 'Select Tariff', 'style': 'width: 100%;'}))
    # room_type = forms.ModelChoiceField(
    #     queryset=AvailableRoomsTypeModel.objects.all(),
    #     widget=forms.Select(attrs={'class': 'select_room_type'})
    # )

