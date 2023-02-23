from django.db import models
from apps.account.models import Account
from apps.warehouse.models.income import IncomeModel
from apps.warehouse.models.items import ItemsModel


class IncomeItemsModel(models.Model):
    income = models.ForeignKey(IncomeModel, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemsModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_by = models.ForeignKey(Account, related_name="income_items", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_income_items", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.income} - {self.item} - {self.quantity}"
