from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.logus.models import *
from apps.logus.models.room import TariffXTypeModel
from apps.logus.models import available_rooms


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


@admin.register(BookedRoomTariffsModel)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in BookedRoomTariffsModel._meta.fields]
    raw_id_fields = ["booked_room"]


@admin.register(BookedRoomRoomModel)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in BookedRoomRoomModel._meta.fields]
    raw_id_fields = ["booked_room"]


@admin.register(Payments)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in Payments._meta.fields]


@admin.register(available_rooms.AvailableRoomModel)
class AvailableRoomModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in available_rooms.AvailableRoomModel._meta.fields]


@admin.register(available_rooms.AvailableRoomsTypeModel)
class AvailableRoomsTypeModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in available_rooms.AvailableRoomsTypeModel._meta.fields]


@admin.register(available_rooms.RoomTypeMatrix)
class RoomTypeMatrixAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in available_rooms.RoomTypeMatrix._meta.fields]
