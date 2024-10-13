from django.urls import path, include

from apps.sanatorium.views.doctors import main_screen, appointments, main_list_of

app_name = 'sanatorium_doctors'


urlpatterns = [
    path('main_screen/', main_screen.main_screen_view, name='main_screen'),
    path('patients/', main_screen.get_patients_list, name='assigned_patients'),

    path('lab-sereachs/<int:pk>', main_screen.get_labs_view, name='get_labs'),

    path('get-patient/<int:pk>', main_screen.get_patient_by_id_view, name='get_patient_by_id'),
    path('notifications/', main_screen.main_screen_view, name='notifications'),
    path('get-bookings-by-start-date', main_screen.get_bookings_by_start_date_view, name='by-start-date'),

    path('appointments/init-app/<int:pk>', appointments.get_init_app_by_id_view, name='init_app_page'),
    path('appointments/title-page/<int:pk>', appointments.get_title_page_by_id_view, name='title_page'),
    path('appointments/final-appointment-page/<int:pk>', appointments.final_appointment_view, name='final_appointment_page'),
    path('appointments/cardiologist-appointment-page/<int:pk>', appointments.cardiologist_appointment_view, name='cardiologist_appointment_page'),
    path('appointments/neurologist-appointment-page/<int:pk>', appointments.neurologist_appointment_view, name='neurologist_appointment_page'),
    path('appointments/on-arrival-appointment-page/<int:pk>', appointments.on_arrival_appointments_view, name='on_arrival_appointment_page'),
    path('appointments/repeated-appointment-page/<int:pk>', appointments.repeated_appointments_view, name='repeated_appointments_page'),
    path('appointments/update-repeated-appointment-page/<int:pk>', appointments.update_repeated_appointments_view, name='update_repeated_appointments_page'),

    path('appointments/with-doc-on-duty-appointment-page/<int:pk>', appointments.with_doc_on_duty_appointment_view, name='with_doc_on_duty_appointment_page'),
    path('appointments/update-with-doc-on-duty-appointment-page/<int:pk>', appointments.update_with_doc_on_duty_appointment_view, name='update_with_doc_on_duty_appointment_page'),
    path('appointments/ekg-appointment-page/<int:pk>', appointments.ekg_appointment_view, name='ekg_appointment_page'),
    path('appointments/update-ekg-appointment-page/<int:pk>', appointments.update_ekg_appointment_view, name='update_ekg_appointment_page'),

    path('patients/list-of-procedures/<int:pk>', main_list_of.main_list_of_procedures_view, name='main_list_of_procedures'),
    path('patients/treatment-proc-update/<int:pk>', main_list_of.treatment_procedure_update, name='treatment_procedure_update'),
    path('patients/pills-injections-update/<int:pk>', main_list_of.pills_injections_update, name='pills_injections_update'),
    path('patients/consulting-update/<int:pk>', main_list_of.consulting_update, name='consulting_update'),
]

