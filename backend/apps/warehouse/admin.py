from django.contrib import admin

from apps.warehouse.models import *


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
admin.site.register(WarehouseChequeModel)
admin.site.register(ChequeItemsModel)
