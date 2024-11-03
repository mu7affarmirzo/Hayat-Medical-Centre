import random

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.account.models import Account, PatientModel
from apps.sanatorium.models import IllnessHistory
from apps.warehouse.models import ItemsModel, ItemsInStockModel


class WarehouseChequeModel(models.Model):
    STATE_CHOICES = (
        ('оплачено', 'оплачено'),
        ('отменена', 'отменена'),
        ('не оплачено', 'не оплачено'),
    )

    cheque_number = models.CharField(max_length=15, blank=True, unique=True)
    patient = models.ForeignKey(PatientModel, related_name='w_cheque_p', on_delete=models.SET_NULL, null=True,
                                blank=True)
    state = models.CharField(choices=STATE_CHOICES, default='не оплачено', max_length=50)
    illness_history = models.OneToOneField(
        IllnessHistory, on_delete=models.CASCADE,
        null=True, related_name='warehouse_cheque'
    )

    is_sanatorium_based = models.BooleanField(default=False, null=True, blank=True)

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
            summ += i.overall_price
        return summ


class ChequeItemsModel(models.Model):
    STATE_CHOICES = (
        ('assigned', 'assigned'),
        ('accepted', 'accepted'),
        ('cancelled', 'cancelled'),
        ('stopped', 'stopped'),
        ('dispatched', 'dispatched'),
    )
    PILLS_FREQUENCY_CHOICES = (
        ("3 раза в день", "3 раза в день"),
        ("до еды", "до еды"),
        ("после еды", "после еды"),
    )

    cheque = models.ForeignKey(WarehouseChequeModel, on_delete=models.CASCADE, related_name='cheque_items', null=True)
    item = models.ForeignKey(ItemsInStockModel, on_delete=models.SET_NULL, null=True)

    price = models.IntegerField(default=0)  # ItemsInStock modeldan unit_price keladi

    quantity = models.IntegerField(default=1)

    state = models.CharField(choices=STATE_CHOICES, default='assigned', max_length=50)
    quantity_per_session = models.IntegerField(default=1, null=True, blank=True)
    period_days = models.IntegerField(null=True, blank=True)
    frequency = models.CharField(choices=PILLS_FREQUENCY_CHOICES, default='', max_length=50)
    comments = models.TextField(null=True, blank=True)
    instruction = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    created_by = models.ForeignKey(Account, related_name="warehouse_cheque_item", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="w_edit_cheque_item", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.cheque} - {self.item}"

    @property
    def overall_price(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        frequency_map = {
            "3 раза в день": 3,
            "до еды": 1,
            "после еды": 1,
        }

        # Get the integer value of the frequency
        frequency_value = frequency_map.get(self.frequency, 1)  # Default to 1 if not found


        if self.pk:
            # The instance already exists, so it's an update
            previous_instance = ChequeItemsModel.objects.get(pk=self.pk)
            quantity_difference = self.quantity - previous_instance.quantity
        else:
            quantity_difference = self.quantity

        # Update the quantity of the item in stock
        if self.item:
            self.item.unit_quantity -= quantity_difference
            self.price = self.item.unit_price
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
