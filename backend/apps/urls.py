from django.urls import path, include

urlpatterns = [
    # path('warehouse/v1/', include('apps.warehouse.urls.v1')),
    path('warehouse/', include('apps.warehouse.urls.v2')),
    path('warehouse/manual/', include('apps.warehouse.urls.manual')),
    path('warehouse/branch/', include('apps.warehouse.urls.branch')),
    # path('hospital/', include('apps.hospital.urls')),

]
