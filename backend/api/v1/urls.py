from django.urls import path, include

urlpatterns = [
    # path('account/', include('api.v1.account.urls')),
    # path('organizations/', include('api.v1.organizations.urls')),
    # path('doctors/', include('api.v1.doctors.urls')),
    # path('appointments/', include('api.v1.appointment.urls')),
    # path('cashbox/', include('api.v1.cashbox.urls')),
    # path('warehouse/', include('api.v1.warehouse.urls')),
    path('logus/', include('api.v1.logus.urls')),
]
