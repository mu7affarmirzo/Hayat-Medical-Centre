from django.urls import path, include

from apps.sanatorium.views.dispatcher import patients, dispatchs

app_name = 'sanatorium_dispatchers'


urlpatterns = [
    path('patients/', patients.get_patients_list, name='main_screen'),

    path('get-patient-procedures/<int:pk>', patients.get_patient_procedures_view, name='patient_procedures'),
    path('notifications/', patients.get_patients_list, name='notifications'),
    path('get-bookings-by-start-date', patients.get_bookings_by_start_date_view, name='by-start-date'),


    path('action/', dispatchs.get_waiting_list, name='get_waiting_dispatch'),
    path('action/dispatch-patient-procedure/<int:pk>', patients.dispatch_patient_procedures_view, name='patient_procedure_dispatch'),
    path('actions/get-patient-procedure-by-days/<int:pk>', patients.get_patient_procedure_by_days_view, name='patient_procedure_by_days'),
    path('action/update-procedure-days/<int:pk>', patients.update_procedure_days_view, name='update_procedure_days'),
]

