from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from api.v1.account.services.email import send_email
from apps.account.models.accounts import Account
from apps.warehouse.models.store_point import StorePointModel


class SendRegistryModel(models.Model):
    receiver = models.ForeignKey(StorePointModel, related_name="send_reg_receiver", on_delete=models.CASCADE)
    sender = models.ForeignKey(StorePointModel, related_name="send_reg_sender", on_delete=models.CASCADE)
    is_delivered = models.BooleanField(default=False)
    created_by = models.ForeignKey(Account, related_name="send_registry", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_send_registry", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.receiver} - {self.sender} - {self.is_delivered}"


@receiver(post_save, sender=SendRegistryModel)
def send_email_to_receiver(sender, instance: SendRegistryModel = None, created=False, **kwargs):
    if created:
        send_email(instance.receiver.email, f"From {instance.sender.name} sent some items\n id: {instance.id}")
    elif instance.is_delivered:
        send_email(instance.sender.email, f"Delivered \n id:{instance.id}")

    # TODO: please edit email message text
