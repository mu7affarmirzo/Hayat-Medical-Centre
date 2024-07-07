from apps.warehouse.models import ItemsInStockModel


def in_stock_by_item_sender(item, warehouse):
    try:
        target_item = ItemsInStockModel.objects.get(item=item, warehouse=warehouse)
    except ItemsInStockModel.DoesNotExist:
        return None
    except ItemsInStockModel.MultipleObjectsReturned:
        return ItemsInStockModel.objects.filter(item=item, warehouse=warehouse).first()
    return target_item
