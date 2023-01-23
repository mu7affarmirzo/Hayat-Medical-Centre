from django.urls import path
from api.v1.cashbox.views.cashbox_closing import CashBoxView
from api.v1.cashbox.views.receipt import ReceiptView, ReceiptRetrieveView
from api.v1.cashbox.views.transactions import TransactionsView, transactions_time_view, RetrieveTransactionsView, \
    get_by_tr_id_view, transactions_type_filter, get_by_duty_id_view

urlpatterns = [
    path('receipt', ReceiptView.as_view(), name='receipt'),
    path('receipt/<int:pk>', ReceiptRetrieveView.as_view(), name='receipt - pk'),
    path('cashbox', CashBoxView.as_view(), name='cashbox'),
    # path('cashbox/<int:pk>', CashBoxRetrieveView.as_view(), name='receipt - pk'),
    path('transactions/', TransactionsView.as_view(), name='transactions'),
    path('transactions/appointment/<int:pk>', RetrieveTransactionsView.as_view(), name='transactions'),
    path('transactions/<int:pk>', get_by_tr_id_view, name='tr-by-id'),
    path('transactions/duty/<int:pk>', get_by_duty_id_view, name='tr-by-duty-id'),
    path('transactions-with-time/', transactions_time_view, name='transactions-with-time'),
    path('transactions-type-filter/', transactions_type_filter, name='transactions-type-filter'),
]
