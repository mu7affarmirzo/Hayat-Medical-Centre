from django.urls import path, include

from apps.logus.views import auth, bookings

app_name = 'sanatorium_staff'

urlpatterns = [
    path('', auth.login_view, name='login'),
    path('main_screen/', auth.main_screen_view, name='main_screen'),
    path('available-rooms/', auth.available_room_view, name='available-rooms'),
]
