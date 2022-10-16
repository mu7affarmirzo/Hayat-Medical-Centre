from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from api.v1.account.views.login import CustomTokenObtainPairView

app_name = 'account'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('custom-login/', CustomTokenObtainPairView.as_view(), name='custom-token_obtain_pair'),
]
