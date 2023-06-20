from django.urls import path, include

from apps.warehouse.views import login_view, index_view, IncomeView, MedicinesView, logout_view

app_name = 'warehouse'

urlpatterns = [
    path('login/', login_view, name='warehouse-login'),
    path('logout/', logout_view, name='warehouse-logout'),
    path('index/', index_view, name='warehouse-index'),
    path('incomes/', IncomeView.as_view(), name='warehouse-incomes'),
    path('medicines/', MedicinesView.as_view(), name='warehouse-medicines'),
]
