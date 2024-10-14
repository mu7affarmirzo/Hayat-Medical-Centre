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
    serial = models.CharField(default=uuid.uuid4, max_length=255, unique=True)
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

    @property
    def overall_summ(self):
        summ = 0
        items = self.income_items.all()
        for item in items:
            summ += item.overall_price
        return summ


class IncomeItemsModel(models.Model):
    income = models.ForeignKey(IncomeModel, on_delete=models.CASCADE, related_name="income_items")
    item = models.ForeignKey(ItemsModel, on_delete=models.CASCADE)
    price = models.BigIntegerField(default=0, null=True, blank=True)
    unit_price = models.BigIntegerField(default=0, null=True, blank=True)
    nds = models.PositiveIntegerField(default=0, null=True, blank=True)
    overall_price = models.BigIntegerField(default=0, null=True, blank=True)
    quantity = models.IntegerField()
    unit_quantity = models.IntegerField(null=True, default=0, blank=True)
    expire_date = models.DateField(null=True)
    created_by = models.ForeignKey(Account, related_name="income_items", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_income_items", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.income} - {self.item} - {self.quantity}"


@receiver(pre_save, sender=IncomeItemsModel)
def income_item_overall_price(sender, instance, **kwargs):
    if instance.nds != 0:
        instance.unit_price = int(instance.unit_price*(100+instance.nds)/100)
        instance.price = instance.unit_price*instance.item.in_pack

    instance.overall_price = ((instance.quantity*instance.item.in_pack) + instance.unit_quantity) * instance.unit_price


@receiver(post_save, sender=IncomeItemsModel)
def items_to_stock(sender, instance: IncomeItemsModel, created, **kwargs):
    if created:
        print('------------ created ---------------')
        ItemsInStockModel.objects.create(
            item=instance.item,
            income_seria=instance.income.serial,
            quantity=instance.quantity,
            unit_quantity=instance.unit_quantity,
            expire_date=instance.expire_date,
            warehouse=instance.income.receiver,
            price=instance.price,
            unit_price=instance.unit_price
        )
    else:
        print('------------ ELSE ---------------')
        print(instance.income.serial)
        print(instance.item)
        print(instance.income.receiver)
        items_in_stock = ItemsInStockModel.objects.filter(
            income_seria=instance.income.serial,
            item=instance.item,
            warehouse=instance.income.receiver
        )
        print(f'------------ {items_in_stock} ---------------')
        for stock_item in items_in_stock:
            stock_item.price = instance.price
            stock_item.unit_price = instance.unit_price
            stock_item.save()


@receiver(post_save, sender=IncomeModel)
def create_income_serial_number(sender, instance=None, created=False, **kwargs):
    if created:
        number_str = str(instance.id).zfill(5)
        instance.serial = f"{instance.serial}|{number_str}"
        instance.save()