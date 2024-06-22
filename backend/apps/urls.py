from django.urls import path, include

urlpatterns = [
    # path('warehouse/v1/', include('apps.warehouse.urls.v1')),
    path('warehouse/v2/', include('apps.warehouse.urls.v2')),
    # path('hospital/', include('apps.hospital.urls')),

]
