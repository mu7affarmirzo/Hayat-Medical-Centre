import uuid
from django.db import models
from apps.account.models.accounts import Account
from apps.warehouse.models.store_point import StorePointModel


class IncomeModel(models.Model):
    serial = models.UUIDField(default=uuid.uuid4())
    receiver = models.ForeignKey(StorePointModel, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Account, related_name="income", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_income", on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.receiver} - {self.serial}"


