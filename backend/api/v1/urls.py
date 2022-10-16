from django.urls import path, include

urlpatterns = [
    path('account/', include('api.v1.account.urls')),
    path('organizations/', include('api.v1.organizations.urls')),
]