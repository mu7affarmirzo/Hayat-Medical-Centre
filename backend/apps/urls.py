from django.urls import path, include

urlpatterns = [
    # path('warehouse/v1/', include('apps.warehouse.urls.v1')),
    path('warehouse/', include('apps.warehouse.urls.v2')),
    path('warehouse/manual/', include('apps.warehouse.urls.manual')),
    path('warehouse/branch/', include('apps.warehouse.urls.branch')),
    path('warehouse/storepoint/', include('apps.warehouse.urls.storepoint')),
    path('warehouse/company/', include('apps.warehouse.urls.company')),

    path('logus/', include('apps.logus.urls')),
    path('sanatorium/', include('apps.sanatorium.urls')),

]
