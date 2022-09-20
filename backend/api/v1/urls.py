from django.urls import path, include

urlpatterns = [
    path('account/', include('api.v1.account.urls')),
]