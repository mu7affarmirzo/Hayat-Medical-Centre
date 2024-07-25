from django.urls import path, include

from apps.logus.views import auth

app_name = 'logus_auth'

urlpatterns = [
    path('', auth.login_view, name='login'),
    path('main_screen/', auth.main_screen_view, name='main_screen'),
    # path('manual/', include('apps.logus.urls.manual')),
    # path('branch/', include('apps.logus.urls.branch')),
    # path('storepoint/', include('apps.logus.urls.storepoint')),
    # path('company/', include('apps.logus.urls.company')),

]
