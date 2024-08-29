from django.urls import path, include

from apps.logus.views import bookings

app_name = 'sanatorium_nurses'

urlpatterns = [
    path('check-in', bookings.get_upcoming_check_ins_view, name='check-in'),
    path('get-bookings', bookings.get_bookings_view, name='get-bookings'),
]