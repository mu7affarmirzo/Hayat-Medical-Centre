from django.db import models
from apps.account.models.accounts import Account
from apps.warehouse.models.send_registry import SendRegistryModel
from apps.warehouse.models.store_point import StorePointModel


class ReceiveRegistryModel(models.Model):
    send_registry = models.ForeignKey(SendRegistryModel, on_delete=models.CASCADE)
    receiver = models.ForeignKey(StorePointModel, related_name="rece_reg_receiver", on_delete=models.CASCADE)
    sender = models.ForeignKey(StorePointModel, related_name="rece_reg_sender", on_delete=models.CASCADE)
    created_by = models.ForeignKey(Account, related_name="receive_registry", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_receive_registry", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.sender} - {self.receiver} - {self.send_registry}"