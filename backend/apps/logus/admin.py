from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.logus.models import *
from apps.logus.models.room import TariffXTypeModel


@admin.register(RoomModel)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["room_number", "is_available", "count", "floor", "view", "room_type", "capacity", "created_by",
                    # "created_at", "modified_at",
                    "modified_by"]


@admin.register(BookedRoomModel)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in BookedRoomModel._meta.fields]
    # list_display = ["room_price", "room", "patients", "discount", "abs_price", "is_checked_out", "start_date",
    #                 "end_date", "created_by", "modified_by"]


@admin.register(TariffModel)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in TariffModel._meta.fields]


@admin.register(RoomTypeModel)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in RoomTypeModel._meta.fields]


@admin.register(BookingModel)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in BookingModel._meta.fields]


@admin.register(ServiceModel)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in ServiceModel._meta.fields]


@admin.register(TariffServiceModel)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in TariffServiceModel._meta.fields]


@admin.register(RoomPrice)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in RoomPrice._meta.fields]


@admin.register(TariffXTypeModel)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in TariffXTypeModel._meta.fields]


@admin.register(LogusChequeModel)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in LogusChequeModel._meta.fields]


@admin.register(AdditionallyPurchasedServicesModel)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in AdditionallyPurchasedServicesModel._meta.fields]
    raw_id_fields = ["booked_room"]