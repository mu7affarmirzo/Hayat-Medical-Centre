from django.urls import path

from apps.logus.views import payment

app_name = 'logus_payment'

urlpatterns = [
    path('debtors-list', payment.get_debtors_list, name='debtors_list'),
    path('debtor-detailed/<int:pk>', payment.get_debtor_detailed, name='debtor_detailed'),
    path('proceed-payment/<int:pk>', payment.proceed_payment, name='proceed_payment'),
]