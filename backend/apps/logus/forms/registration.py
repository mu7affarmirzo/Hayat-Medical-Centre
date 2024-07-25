from django import forms


class DateRangeForm(forms.Form):
    reservation_time = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control float-right',
        'id': 'reservationtime',
    }))

