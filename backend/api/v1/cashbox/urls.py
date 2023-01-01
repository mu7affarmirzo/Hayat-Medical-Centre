from django.urls import path, include
from api.v1.cashbox.views.cashbox_closing import *
from api.v1.cashbox.views.receipt import ReceiptView, ReceiptRetrieveView

urlpatterns = [
    path('receipt', ReceiptView.as_view(), name='receipt'),
    path('receipt/<int:pk>', ReceiptRetrieveView.as_view(), name='receipt - pk'),
    path('cashbox', CashBoxView.as_view(), name='cashbox'),
    path('cashbox/<int:pk>', CashBoxRetrieveView.as_view(), name='receipt - pk')
]