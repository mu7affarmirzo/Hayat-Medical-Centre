from django.urls import path, include

from apps.logus.views import auth

app_name = 'sanatorium_doctors'

urlpatterns = [
    path('', auth.login_view, name='login'),
    path('logout/', auth.logout_view, name='logout'),
    path('main_screen/', auth.main_screen_view, name='main_screen'),

]
