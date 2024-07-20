from apps.warehouse.models import ItemsInStockModel


def in_stock_by_item_sender(item, warehouse):
    try:
        target_item = ItemsInStockModel.objects.get(item=item, warehouse=warehouse)
    except ItemsInStockModel.DoesNotExist:
        return None
    except ItemsInStockModel.MultipleObjectsReturned:
        return ItemsInStockModel.objects.filter(item=item, warehouse=warehouse).first()
    return target_item


def add_to_warehouse(series, warehouse, item, expire_date, quantity):
    try:
        target_item = ItemsInStockModel.objects.get(item=item, warehouse=warehouse)
    except ItemsInStockModel.DoesNotExist:
        ItemsInStockModel.objects.create(
            income_seria=series,
            warehouse=warehouse,
            item=item, expire_date=expire_date,
            quantity=quantity
        )
        return True
    except ItemsInStockModel.MultipleObjectsReturned:
        return False

    target_item.quantity += quantity
    target_item.save()
    return True


def remove_from_warehouse(item, warehouse, quantity):
    try:
        target_item = ItemsInStockModel.objects.get(item=item, warehouse=warehouse)
    except ItemsInStockModel.DoesNotExist:
        return False
    except ItemsInStockModel.MultipleObjectsReturned:
        return False
    target_item.quantity -= quantity
    target_item.save()
    return True
