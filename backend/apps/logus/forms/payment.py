from django import forms
from apps.logus.models import Payments


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payments
        fields = [
            'payment_name', 'comment',
            'transaction_type',
        ]


