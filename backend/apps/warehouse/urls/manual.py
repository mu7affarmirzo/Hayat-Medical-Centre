from django.urls import path
from apps.warehouse.views import manual

app_name = 'warehouse_manual'

urlpatterns = [
    path('main-screen/', manual.main_screen_view, name='main_screen'),

    path('add-items/', manual.add_items_view, name='add-items'),
    path('items-list/', manual.items_list_view, name='items-list'),
]
