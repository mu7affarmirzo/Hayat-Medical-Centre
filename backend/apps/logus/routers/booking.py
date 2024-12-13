from django.urls import path, include

from apps.logus.views import bookings

app_name = 'logus_booking'

urlpatterns = [
    path('check-in', bookings.get_upcoming_check_ins_view, name='check-in'),
    path('check-in/update/<int:pk>', bookings.update_check_in_view, name='check-in-update'),
    path('get-bookings', bookings.get_bookings_view, name='get-bookings'),

    path('living', bookings.get_living_guests, name='living'),

    path('check-out', bookings.get_upcoming_checkouts, name='check-out'),
    path('get-checkout-bookings', bookings.get_leaving_bookings_view, name='get-checkout-bookings'),
]