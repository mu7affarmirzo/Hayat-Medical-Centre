from django.db import models
from apps.account.models import Account

PAYMENT_TYPE = (
    ("CASH", "CASH"),
    ("CARD", "CARD"),
)

TYPE = (
    ("INCOME", "INCOME"),
    ("OUTCOME", "OUTCOME"),
)


class ReceiptModel(models.Model):

    created_by = models.ForeignKey(Account, related_name="crt_receipt", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_receipt", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)


