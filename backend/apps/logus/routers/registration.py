from django.urls import path, include

from apps.logus.views import auth, bookings

app_name = 'logus_registration'

urlpatterns = [
    path('', auth.login_view, name='login'),
    path('main_screen/', auth.main_screen_view, name='main_screen'),
    path('test/', auth.test_view, name='test'),
    path('upcoming-checkouts/', bookings.get_upcoming_checkouts, name='get_upcoming_checkouts'),
    # path('date_range/', auth.date_range, name='date_range'),
    # path('manual/', include('apps.logus.urls.manual')),
    # path('branch/', include('apps.logus.urls.branch')),
    # path('storepoint/', include('apps.logus.urls.storepoint')),
    # path('company/', include('apps.logus.urls.company')),

]
