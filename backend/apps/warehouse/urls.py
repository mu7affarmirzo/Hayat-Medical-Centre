from django.urls import path, include

from apps.warehouse.views import LoginViewStatic, IndexView, IncomeView, MedicinesView

app_name = 'warehouse'

urlpatterns = [
    path('login/', LoginViewStatic.as_view(), name='warehouse-login'),
    path('index/', IndexView.as_view(), name='warehouse-index'),
    path('incomes/', IncomeView.as_view(), name='warehouse-incomes'),
    path('medicines/', MedicinesView.as_view(), name='warehouse-medicines'),
]
