from django.db import models

from apps.account.models import Account
from apps.warehouse.models.company import CompanyModel


class ItemsModel(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    in_pack = models.IntegerField(null=True, blank=True, default=10)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    unit = models.CharField(max_length=255, default="shtuk")
    seria = models.CharField(max_length=255, default="")
    is_expired = models.BooleanField(default=False)
    created_by = models.ForeignKey(Account, related_name="item", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_item", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.company} - {self.name} - {self.is_expired}"

    @property
    def validity_color(self):
        # 32a852 - green
        # ebeb17 - yellow
        # #171716 - black
        return 1


class ItemsInStockModel(models.Model):
    income_registry = models.ForeignKey('IncomeModel', on_delete=models.SET_NULL, null=True)
    income_seria = models.CharField(max_length=255, null=True, blank=True)
    item = models.ForeignKey(ItemsModel, on_delete=models.CASCADE, related_name="in_stock")
    quantity = models.IntegerField()
    expire_date = models.DateField(null=True)
    warehouse = models.ForeignKey('StorePointModel', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('item', 'warehouse')
        