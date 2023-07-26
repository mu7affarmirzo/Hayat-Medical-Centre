from django.urls import path, include

urlpatterns = [
    path('warehouse/', include('apps.warehouse.urls')),
    path('hospital/', include('apps.hospital.urls')),

]
