from import_export.admin import ImportExportModelAdmin

from apps.massage.models.purchases import *
from apps.massage.models.services import *

from django.contrib import admin


@admin.register(SessionModel)
class SessionModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in SessionModel._meta.fields]


@admin.register(PaymentModel)
class PaymentModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in PaymentModel._meta.fields]


@admin.register(ServiceModel)
class ServiceModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in ServiceModel._meta.fields]


@admin.register(ServiceTypeModel)
class ServiceTypeModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in ServiceTypeModel._meta.fields]

