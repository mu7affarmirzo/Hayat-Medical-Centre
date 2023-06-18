from django.urls import path, include

from apps.warehouse.views import LoginViewStatic

urlpatterns = [
    path('login/', LoginViewStatic.as_view(), name='warehouse-login'),
]
