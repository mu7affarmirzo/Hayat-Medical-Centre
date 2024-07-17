import uuid

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from apps.account.models.accounts import Account
from apps.warehouse.models import ItemsModel, ItemsInStockModel
from apps.warehouse.models.store_point import StorePointModel


class IncomeModel(models.Model):
    STATE_CHOICES = (
        ('в ожидании', 'в ожидании'),
        ('принято', 'принято'),
        ('отказоно', 'отказоно'),
    )
    serial = models.UUIDField(default=uuid.uuid4)
    delivery_company = models.ForeignKey('CompanyModel', on_delete=models.SET_NULL, null=True, blank=True)
    receiver = models.ForeignKey(StorePointModel, on_delete=models.CASCADE)
    bill_amount = models.BigIntegerField(default=0, null=True, blank=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=50, default='принято')
    created_by = models.ForeignKey(Account, related_name="income", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_income", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.receiver} - {self.serial}"


class IncomeItemsModel(models.Model):
    income = models.ForeignKey(IncomeModel, on_delete=models.CASCADE, related_name="income_items")
    item = models.ForeignKey(ItemsModel, on_delete=models.CASCADE)
    price = models.BigIntegerField(default=0, null=True, blank=True)
    overall_price = models.BigIntegerField(default=0, null=True, blank=True)
    quantity = models.IntegerField()
    expire_date = models.DateField(null=True)
    created_by = models.ForeignKey(Account, related_name="income_items", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_income_items", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.income} - {self.item} - {self.quantity}"


@receiver(pre_save, sender=IncomeItemsModel)
def income_item_overall_price(sender, instance, **kwargs):
    instance.overall_price = instance.quantity * instance.price


@receiver(post_save, sender=IncomeItemsModel)
def items_to_stock(sender, instance: IncomeItemsModel, created, **kwargs):
    if created:
        ItemsInStockModel.objects.create(
            item=instance.item,
            income_seria=instance.income.serial,
            quantity=instance.quantity,
            expire_date=instance.expire_date,
            warehouse=instance.income.receiver,
            price=instance.price
        )
