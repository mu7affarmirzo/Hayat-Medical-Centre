from django.urls import path, include

from apps.sanatorium.views import staff

app_name = 'sanatorium_staff'

urlpatterns = [
    path('main_screen/', staff.main_screen_view, name='main_screen'),
    path('patients/', staff.get_patients_list, name='patients'),
    path('get-patient/<int:pk>', staff.get_patient_by_id_view, name='get_patient_by_id'),
    path('notifications/', staff.main_screen_view, name='notifications'),
    path('get-bookings-by-start-date', staff.get_bookings_by_start_date_view, name='by-start-date'),
]
