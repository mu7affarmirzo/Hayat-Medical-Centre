from django.db import models

from apps.account.models import Account
from apps.warehouse.models.items import ItemsModel
from apps.warehouse.models.send_registry import SendRegistryModel


class SentItemsModel(models.Model):
    item = models.ForeignKey(ItemsModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    send_registry = models.ForeignKey(SendRegistryModel, on_delete=models.CASCADE)
    is_delivered = models.BooleanField()
    created_by = models.ForeignKey(Account, related_name="sent_items", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_sent_items", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.item} - {self.quantity} - {self.quantity}"