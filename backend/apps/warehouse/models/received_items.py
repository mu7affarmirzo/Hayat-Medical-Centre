from django.db import models

from apps.account.models import Account
from apps.warehouse.models.items import ItemsModel
from apps.warehouse.models.receive_registry import ReceiveRegistryModel


class ReceivedItemsModel(models.Model):
    item = models.ForeignKey(ItemsModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    received_registry = models.ForeignKey(ReceiveRegistryModel, on_delete=models.CASCADE, related_name="received_items")
    created_by = models.ForeignKey(Account, related_name="recevid_items", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_recevid_items", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.item} - {self.quantity} - {self.received_registry}"

    @property
    def filial(self):
        return self.received_registry.send_registry.sender.name

    @property
    def summary_price(self):
        return self.item.price * self.quantity

