from django.urls import path
from apps.warehouse.views.v2 import auth, items

app_name = 'warehouse_v2'

urlpatterns = [
    path('login/', auth.login_view, name='v2-login'),
    path('items/', items.get_items, name='v2-items'),
    path('items-search/', items.search_items, name='v2-items-search'),
]
