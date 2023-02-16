from django.db import models
from apps.account.models.accounts import Account
from apps.warehouse.models.store_point import StorePointModel


class SendRegistryModel(models.Model):
    receiver = models.ForeignKey(StorePointModel, related_name="send_reg_receiver", on_delete=models.CASCADE)
    sender = models.ForeignKey(StorePointModel, related_name="send_reg_sender", on_delete=models.CASCADE)
    is_delivered = models.BooleanField()
    created_by = models.ForeignKey(Account, related_name="send_registry", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_send_registry", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.receiver} - {self.sender} - {self.is_delivered}"
