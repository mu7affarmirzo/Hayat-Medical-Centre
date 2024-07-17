from datetime import date

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
        return f"{self.name} - {self.company}"

    @property
    def validity_color(self):
        # 32a852 - green
        # ebeb17 - yellow
        # #171716 - black
        return 1


class ItemsInStockModel(models.Model):
    income_seria = models.CharField(max_length=255, null=True, blank=True)
    item = models.ForeignKey(ItemsModel, on_delete=models.CASCADE, related_name="in_stock")
    quantity = models.IntegerField()
    price = models.IntegerField(default=0)
    expire_date = models.DateField(null=True)
    warehouse = models.ForeignKey('StorePointModel', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item}-{self.income_seria}"

    @property
    def days_until_expire(self):
        if self.expire_date:
            delta = self.expire_date - date.today()
            return delta.days
        return 0

    class Meta:
        unique_together = ('item', 'warehouse', 'expire_date', 'income_seria')
        ordering = ('expire_date', )

