from django.db import models
from apps.account.models import OrganizationModel, BranchModel
from apps.cashbox.models import ReceiptModel


class TransactionsModel(models.Model):
    amount = models.BigIntegerField()
    payment_type = models.IntegerField()
    receipt = models.ForeignKey(ReceiptModel, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(OrganizationModel, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
