from django.contrib import admin
from .models import receipt, cashbox, transactions


# admin.site.register(receipt.ReceiptModel)

@admin.register(receipt.ReceiptModel)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = [field.name for field in receipt.ReceiptModel._meta.fields]


@admin.register(transactions.DutyModel)
class DutyModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in transactions.DutyModel._meta.fields]


@admin.register(cashbox.CashBoxClosingHistoryRecordsModel)
class CashBoxClosingHistoryRecordsModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in cashbox.CashBoxClosingHistoryRecordsModel._meta.fields]


@admin.register(transactions.TransactionsModel)
class TransactionsModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in transactions.TransactionsModel._meta.fields]


@admin.register(transactions.AppointmentServiceTransactionsModel)
class AppointmentServiceTransactionsModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in transactions.AppointmentServiceTransactionsModel._meta.fields]
