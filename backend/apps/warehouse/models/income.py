import uuid

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from apps.account.models.accounts import Account
from apps.warehouse.models import ItemsModel, ItemsInStockModel
from apps.warehouse.models.store_point import StorePointModel


class IncomeModel(models.Model):
    serial = models.UUIDField(default=uuid.uuid4)
    delivery_company = models.ForeignKey('CompanyModel', on_delete=models.SET_NULL, null=True, blank=True)
    receiver = models.ForeignKey(StorePointModel, on_delete=models.CASCADE)
    bill_amount = models.BigIntegerField(default=0, null=True, blank=True)
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


@receiver(post_save, sender=IncomeModel)
def items_to_stock(sender, instance: IncomeModel, created, **kwargs):
    if created:
        income_items = IncomeItemsModel.objects.filter(income=instance)
        for income_item in income_items:
            ItemsInStockModel.objects.create(
                item=income_item,
                income_seria=instance.serial,
                income_registry=instance,
                quantity=income_item.quantity,
                expire_date=income_item.expire_date,
                warehouse=instance.receiver,
                price=income_item.price
            )
