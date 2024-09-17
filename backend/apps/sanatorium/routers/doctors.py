from django.urls import path, include

from apps.sanatorium.views import doctors

app_name = 'sanatorium_doctors'

urlpatterns = [
    path('sidebar/', doctors.sidebar_view, name='sidebar_view'),
    path('main_screen/', doctors.main_screen_view, name='main_screen'),
    path('patients/', doctors.get_patients_list, name='patients'),
    path('get-patient/<int:pk>', doctors.get_patient_by_id_view, name='get_patient_by_id'),
    path('notifications/', doctors.main_screen_view, name='notifications'),
    path('get-bookings-by-start-date', doctors.get_bookings_by_start_date_view, name='by-start-date'),

]
