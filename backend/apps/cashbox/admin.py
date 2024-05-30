from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import receipt, cashbox, transactions


@admin.register(receipt.ReceiptModel)
class ReceiptAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in receipt.ReceiptModel._meta.fields]


@admin.register(transactions.DutyModel)
class DutyModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in transactions.DutyModel._meta.fields]


@admin.register(cashbox.CashBoxClosingHistoryRecordsModel)
class CashBoxClosingHistoryRecordsModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in cashbox.CashBoxClosingHistoryRecordsModel._meta.fields]


@admin.register(transactions.TransactionsModel)
class TransactionsModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in transactions.TransactionsModel._meta.fields]


@admin.register(transactions.AppointmentServiceTransactionsModel)
class AppointmentServiceTransactionsModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in transactions.AppointmentServiceTransactionsModel._meta.fields]
