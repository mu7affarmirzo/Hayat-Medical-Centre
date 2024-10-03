from django.urls import path, include

from apps.sanatorium.views.doctors import main_screen, appointments, main_list_of

app_name = 'sanatorium_doctors'

urlpatterns = [
    path('main_screen/', main_screen.main_screen_view, name='main_screen'),
    path('patients/', main_screen.get_patients_list, name='patients'),

    path('lab-sereachs/<int:pk>', main_screen.get_labs_view, name='get_labs'),

    path('get-patient/<int:pk>', main_screen.get_patient_by_id_view, name='get_patient_by_id'),
    path('notifications/', main_screen.main_screen_view, name='notifications'),
    path('get-bookings-by-start-date', main_screen.get_bookings_by_start_date_view, name='by-start-date'),

    path('appointments/init-app/<int:pk>', appointments.get_init_app_by_id_view, name='init_app_page'),
    path('appointments/title-page/<int:pk>', appointments.get_title_page_by_id_view, name='title_page'),
    path('appointments/final-appointment-page/<int:pk>', appointments.final_appointment_view, name='final_appointment_page'),

    path('patients/list-of-procedures/<int:pk>', main_list_of.main_list_of_procedures_view, name='main_list_of_procedures'),
]


