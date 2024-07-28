import random

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.account.models import Account, PatientModel
from apps.warehouse.models import ItemsModel, ItemsInStockModel


class WarehouseChequeModel(models.Model):
    STATE_CHOICES = (
        ('оплачено', 'оплачено'),
        ('отменена', 'отменена'),
        ('не оплачено', 'не оплачено'),
    )

    cheque_number = models.CharField(max_length=15, blank=True, unique=True)
    patient = models.ForeignKey(PatientModel, related_name='w_cheque_p', on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField(choices=STATE_CHOICES, default='не оплачено', max_length=50)

    created_by = models.ForeignKey(Account, related_name="warehouse_cheque", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="w_edit_cheque", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.cheque_number

    @property
    def total_price(self):
        summ = 0
        for i in self.cheque_items.all():
            summ += (i.item.price * i.quantity)
        return summ


class ChequeItemsModel(models.Model):
    cheque = models.ForeignKey(WarehouseChequeModel, on_delete=models.CASCADE, related_name='cheque_items', null=True)
    item = models.ForeignKey(ItemsInStockModel, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    created_by = models.ForeignKey(Account, related_name="warehouse_cheque_item", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="w_edit_cheque_item", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.cheque} - {self.item}"

    @property
    def price_of_items(self):
        return self.item.price * self.quantity


@receiver(post_save, sender=WarehouseChequeModel)
def create_warehouse_cheque_number(sender, instance=None, created=False, **kwargs):
    if created:
        number_str = str(instance.id).zfill(5)
        instance.cheque_number = number_str
        instance.save()
