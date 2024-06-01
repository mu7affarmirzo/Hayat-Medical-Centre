from django.urls import path
from apps.warehouse.views.v2 import auth

app_name = 'warehouse_v2'

urlpatterns = [
    path('login/', auth.login_view, name='v2-login'),
]
