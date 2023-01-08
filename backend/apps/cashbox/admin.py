from django.contrib import admin
from .models import receipt, cashbox, transactions


# admin.site.register(receipt.ReceiptModel)

@admin.register(receipt.ReceiptModel)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = [field.name for field in receipt.ReceiptModel._meta.fields]


admin.site.register(cashbox.CashBoxClosingHistoryRecordsModel)
admin.site.register(transactions.TransactionsModel)
admin.site.register(transactions.AppointmentServiceTransactionsModel)
