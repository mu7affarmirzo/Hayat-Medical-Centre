from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.warehouse.models import *


def create_admin_class(model):
    return type(
        f"{model.__name__}Admin",
        (ImportExportModelAdmin, admin.ModelAdmin),
        {'list_display': [field.name for field in model._meta.fields]}
    )


for model in [
    ItemsModel, ReceivedItemsModel, ReceiveRegistryModel, SendRegistryModel,
    IncomeModel, IncomeItemsModel, ItemsInStockModel, SentItemsModel,
    StorePointModel, WarehouseChequeModel, ChequeItemsModel, ExpenseModel,
]:
    admin.site.register(model, admin_class=type(
        f"{model.__name__}Admin",
        (ImportExportModelAdmin, admin.ModelAdmin),
        {'list_display': [field.name for field in model._meta.fields]}
    ))


# admin.site.register(ItemsModel, create_admin_class(ItemsModel))
# admin.site.register(ReceivedItemsModel, create_admin_class(ReceivedItemsModel))
# admin.site.register(ReceiveRegistryModel, create_admin_class(ReceiveRegistryModel))
# admin.site.register(SendRegistryModel, create_admin_class(SendRegistryModel))
# admin.site.register(IncomeModel, create_admin_class(IncomeModel))
# admin.site.register(IncomeItemsModel, create_admin_class(IncomeItemsModel))
# admin.site.register(ItemsInStockModel, create_admin_class(ItemsInStockModel))
# admin.site.register(SentItemsModel, create_admin_class(SentItemsModel))
# admin.site.register(StorePointModel, create_admin_class(StorePointModel))
# admin.site.register(WarehouseChequeModel, create_admin_class(WarehouseChequeModel))
# admin.site.register(ChequeItemsModel, create_admin_class(ChequeItemsModel))

@admin.register(CompanyModel)
class CompanyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in CompanyModel._meta.fields]

# @admin.register(CompanyModel)
# class CompanyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = [field.name for field in CompanyModel._meta.fields]
