from django.contrib import admin

from apps.warehouse.models import *

# Register your models here.

admin.site.register(ItemsModel)
admin.site.register(ReceivedItemsModel)
admin.site.register(ReceiveRegistryModel)
admin.site.register(SendRegistryModel)
admin.site.register(IncomeModel)
admin.site.register(IncomeItemsModel)
admin.site.register(ItemsInStockModel)
admin.site.register(CompanyModel)
admin.site.register(SentItemsModel)
admin.site.register(StorePointModel)
