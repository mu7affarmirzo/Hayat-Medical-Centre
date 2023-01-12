from django.db import models
from apps.account.models import OrganizationModel, Account
from apps.account.models import BranchModel


class CashBoxClosingHistoryRecordsModel(models.Model):
    amount = models.BigIntegerField()
    organization = models.ForeignKey(OrganizationModel, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, verbose_name='operationist')
    modified_by = models.ForeignKey(Account, related_name="modf_cashbox", on_delete=models.SET_NULL, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.amount} - {self.created_at} - {self.branch}'


