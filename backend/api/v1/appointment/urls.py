from django.urls import path, include
from api.v1.appointment.views.appointment import AppointmentsModelView, AppointmentsRetrieveView
from api.v1.appointment.views.appointment_service import AppointmentServiceRetrieveView, AppointmentServiceView

app_name = 'appointment'

urlpatterns = [
    path('', AppointmentsModelView.as_view(), name='appointment'),
    path('<int:pk>', AppointmentsRetrieveView.as_view(), name='appointment'),
    path('service/', AppointmentServiceView.as_view(), name='appointment-service'),
    path('service/<int:pk>', AppointmentServiceRetrieveView.as_view(), name='appointment-service'),

]
