from rest_framework_simplejwt.views import TokenObtainPairView

from api.v1.account.serializers.login import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):

    serializer_class = CustomTokenObtainPairSerializer
    token_obtain_pair = TokenObtainPairView.as_view()
