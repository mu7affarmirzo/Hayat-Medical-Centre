from django import forms

from apps.logus.models import TariffModel, AvailableRoomsTypeModel


class DateRangeForm(forms.Form):
    reservation_time = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control float-right',
        'id': 'reservation',
    }))
    tariff = forms.ChoiceField(choices=TariffModel.objects.all(), widget=forms.Select)
    room_type = forms.ChoiceField(choices=AvailableRoomsTypeModel.objects.all(), widget=forms.Select)
