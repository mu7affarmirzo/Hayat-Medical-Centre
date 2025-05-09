from django.urls import path, include

from apps.logus.views import auth

app_name = 'logus_auth'

urlpatterns = [
    path('', auth.login_view, name='login'),
    path('logout/', auth.logout_view, name='logout'),
    path('main_screen/', auth.main_screen_view, name='main_screen'),
    # path('manual/', include('apps.logus.routers.manual')),
    # path('branch/', include('apps.logus.routers.branch')),
    # path('storepoint/', include('apps.logus.routers.storepoint')),
    # path('company/', include('apps.logus.routers.company')),

]
