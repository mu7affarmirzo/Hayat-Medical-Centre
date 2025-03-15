from django.urls import path, include

from apps.massage.views.reception import auth

from apps.massage.views.reception.registration import (
    register_booking_view, add_new_patient, load_services,
    session_detailed_view, singular_payment_view, whole_payment_view
)

app_name = 'massage_reception'

urlpatterns = [
    path('logout/', auth.logout_view, name='logout'),

    path('main_screen/', auth.main_screen_view, name='main_screen'),

    path('not_paid_list/', auth.not_paid_list_view, name='not_paid_list'),


    path('register-session/', register_booking_view, name='register-booking'),
    path('session-detailed/<int:pk>', session_detailed_view, name='session-detailed'),
    path('add-new-patient/', add_new_patient, name='add-new-patient'),
    path('load-services/', load_services, name='load_services'),
    path('make-singular-payment/<int:pk>', singular_payment_view, name='singular_payment'),
    path('make-whole-payment/<int:pk>', whole_payment_view, name='whole_payment'),
]
