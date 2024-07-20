from django.urls import path, include
from apps.warehouse.views.headquerter import manual

app_name = 'warehouse_manual'

urlpatterns = [
    path('main-screen/', manual.main_screen_view, name='main_screen'),

    path('items/', include('apps.warehouse.urls.items')),
]
