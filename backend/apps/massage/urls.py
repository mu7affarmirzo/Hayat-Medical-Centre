from django.urls import path, include


urlpatterns = [
    # path('adminstration/', include('apps.massage.routers.adminstration')),
    path('reception/', include('apps.massage.routers.reception')),
]
