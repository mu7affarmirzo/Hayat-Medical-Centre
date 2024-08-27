from django.urls import path, include

urlpatterns = [
    path('', include('apps.logus.routers.auth')),
    path('registration/', include('apps.logus.routers.registration')),
    path('booking/', include('apps.logus.routers.booking')),
]
