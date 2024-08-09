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
            summ += i.price_of_items
        return summ


class ChequeItemsModel(models.Model):
    cheque = models.ForeignKey(WarehouseChequeModel, on_delete=models.CASCADE, related_name='cheque_items', null=True)
    item = models.ForeignKey(ItemsInStockModel, on_delete=models.SET_NULL, null=True)

    price = models.IntegerField(default=0)# ItemsInStock modeldan unit_price keladi

    quantity = models.IntegerField(default=1)

    created_by = models.ForeignKey(Account, related_name="warehouse_cheque_item", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="w_edit_cheque_item", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.cheque} - {self.item}"

    @property
    def price_of_items(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        if self.pk:
            # The instance already exists, so it's an update
            previous_instance = ChequeItemsModel.objects.get(pk=self.pk)
            quantity_difference = self.quantity - previous_instance.quantity
        else:
            # The instance is new, so it's a creation
            quantity_difference = self.quantity

        # Update the quantity of the item in stock
        if self.item:
            self.item.unit_quantity -= quantity_difference
            self.item.save()

        super().save(*args, **kwargs)


@receiver(post_save, sender=WarehouseChequeModel)
def create_warehouse_cheque_number(sender, instance=None, created=False, **kwargs):
    if created:
        number_str = str(instance.id).zfill(5)
        instance.cheque_number = number_str
        instance.save()


@receiver(post_save, sender=ChequeItemsModel)
def update_cheque_item_price_number(sender, instance=None, created=False, **kwargs):
    if created:
        instance.price = instance.item.unit_price
        instance.save()
        # TODO: update InStockModel
