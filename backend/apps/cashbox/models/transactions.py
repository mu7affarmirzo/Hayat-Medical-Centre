from django.db import models
from apps.account.models import OrganizationModel, BranchModel, Account
from apps.cashbox.models import ReceiptModel


PAYMENT_TYPE = (
    ("CASH", "CASH"),
    ("CARD", "CARD"),
    ("PAYME", "PAYME"),
    ("CLICK", "CLICK"),
)

TYPE = (
    ("INCOME", "INCOME"),
    ("OUTCOME", "OUTCOME"),
)


class TransactionsModel(models.Model):
    amount = models.BigIntegerField()
    payment_type = models.CharField(choices=PAYMENT_TYPE, max_length=50)
    receipt = models.ForeignKey(ReceiptModel, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(OrganizationModel, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Account, related_name="crt_transactions", on_delete=models.SET_NULL, null=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_transactions", on_delete=models.SET_NULL, null=True)
