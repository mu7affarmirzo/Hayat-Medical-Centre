from django.urls import path, include

from apps.logus.views import auth, bookings

app_name = 'logus_registration'

urlpatterns = [
    path('', auth.login_view, name='login'),
    path('main_screen/', auth.main_screen_view, name='main_screen'),
    path('available-rooms/', auth.available_room_view, name='available-rooms'),

    path('register-booking/', auth.register_booking_view, name='register-booking'),
    path('add-new-patient/', auth.add_new_patient, name='add-new-patient'),

    path('upcoming-checkouts/', bookings.get_upcoming_checkouts, name='get_upcoming_checkouts'),

]
