from django.contrib import admin
from .models import receipt, cashbox, transactions


admin.site.register(receipt.ReceiptModel)
admin.site.register(cashbox.CashBoxClosingHistoryRecordsModel)
admin.site.register(transactions.TransactionsModel)
admin.site.register(transactions.AppointmentServiceTransactionsModel)
