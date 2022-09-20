from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView


app_name = 'account'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]