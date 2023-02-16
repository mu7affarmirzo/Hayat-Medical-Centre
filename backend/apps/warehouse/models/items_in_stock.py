from django.db import models

from apps.warehouse.models.items import ItemsModel
from apps.warehouse.models.store_point import StorePointModel


class ItemsInStockModel(models.Model):
    item = models.ForeignKey(ItemsModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    warehouse = models.ForeignKey(StorePointModel, on_delete=models.CASCADE)
