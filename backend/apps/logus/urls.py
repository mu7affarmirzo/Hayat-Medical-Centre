from django.urls import path, include

urlpatterns = [
    path('', include('apps.logus.routers.auth')),
    path('registration/', include('apps.logus.routers.registration')),
    # path('branch/', include('apps.logus.urls.branch')),
    # path('storepoint/', include('apps.logus.urls.storepoint')),
    # path('company/', include('apps.logus.urls.company')),

]
