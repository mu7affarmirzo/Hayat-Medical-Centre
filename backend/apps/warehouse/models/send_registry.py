from decouple import config
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse

from api.v1.account.services.email import send_email
from apps.account.models import NotificationModel
from apps.account.models.accounts import Account
from apps.warehouse.models import ItemsModel, ItemsInStockModel
from apps.warehouse.models.crud.items import in_stock_by_item_sender
from apps.warehouse.models.store_point import StorePointModel, StorePointStaffModel
from datetime import date

HOST = config('PRODUCTION_HOST')


class SendRegistryModel(models.Model):
    STATE_CHOICES = (
        ('в ожидании', 'в ожидании'),
        ('доставлено', 'доставлено'),
        ('отказоно', 'отказоно'),
    )
    series = models.CharField(null=True, blank=True, max_length=255)
    receiver = models.ForeignKey(StorePointModel, related_name="send_reg_receiver", on_delete=models.CASCADE)
    sender = models.ForeignKey(StorePointModel, related_name="send_reg_sender", on_delete=models.CASCADE)
    state = models.CharField(choices=STATE_CHOICES, default='в ожидании', max_length=50)
    is_delivered = models.BooleanField(default=False)
    created_by = models.ForeignKey(Account, related_name="send_registry", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_send_registry", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.receiver} - {self.sender} - {self.is_delivered}"

    def __init__(self, *args, **kwargs):
        super(SendRegistryModel, self).__init__(*args, **kwargs)
        self.__original_state = f"{self.state}"


class SentItemsModel(models.Model):
    STATE_CHOICES = (
        ('в ожидании', 'в ожидании'),
        ('отменена', 'отменена'),
        ('не найдено', 'не найдено'),
        ('принято', 'принято'),

    )
    item = models.ForeignKey(ItemsInStockModel, on_delete=models.CASCADE, related_name="send_registry_items")
    expire_date = models.DateField(null=True)
    state = models.CharField(choices=STATE_CHOICES, default='принято', max_length=50)
    quantity = models.IntegerField()
    send_registry = models.ForeignKey(SendRegistryModel, on_delete=models.CASCADE, related_name='send_registry_items')
    is_delivered = models.BooleanField(default=False)
    created_by = models.ForeignKey(Account, related_name="sent_items", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_sent_items", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.item} - {self.quantity} - {self.quantity}"

    @property
    def days_until_expire(self):
        if self.expire_date:
            delta = self.expire_date - date.today()
            return delta.days
        return 0


@receiver(post_save, sender=SendRegistryModel)
def create_notification_to_receiver(sender, instance: SendRegistryModel = None, created=False, **kwargs):
    if created:
        receiver = instance.receiver
        target_receivers = StorePointStaffModel.objects.filter(
            store_point=receiver
        )
        for user in target_receivers:
            url = reverse('warehouse_v2:transfers-detailed', args=[instance.id])

            NotificationModel.objects.create(
                sender=instance.created_by,
                receiver=user.staff,
                message='Вам отправили новый <<Приход>>!',
                generated_url=url
            )


@receiver(post_save, sender=SentItemsModel)
def update_items_in_stock(sender, instance: SentItemsModel = None, created=False, **kwargs):

    if created:
        senders_item = instance.item
        senders_item.quantity -= instance.quantity
        senders_item.save()


# @receiver(post_save, sender=SendRegistryModel)
# def send_email_to_receiver(sender, instance: SendRegistryModel = None, created=False, **kwargs):
#     if created:
#         send_email(instance.receiver.email, f"From {instance.sender.name} sent some items\n id: {instance.id}")
#     elif instance.is_delivered:
#         send_email(instance.sender.email, f"Delivered \n id:{instance.id}")
#
#     # TODO: please edit email message text
