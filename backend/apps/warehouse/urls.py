from django.urls import path, include

from apps.warehouse.views import main

app_name = 'warehouse'

urlpatterns = [
    path('login/', main.login_view, name='warehouse-login'),
    path('logout/', main.logout_view, name='warehouse-logout'),
    path('index/', main.index_view, name='warehouse-index'),
    path('incomes/', main.incomes_view, name='warehouse-incomes'),
    path('incomes/<int:pk>', main.incomes_view, name='warehouse-incomes'),
    path('medicines/', main.medicines_view, name='warehouse-medicines'),
    path('medicines/<int:pk>', main.medicines_view, name='warehouse-medicines'),
]
