from django.urls import path, include
from api.v1.doctors.views.medical_service import MedicalServiceRetrieveView,MedicalServiceView
app_name = 'doctors'

urlpatterns = [
    path('services/', MedicalServiceView.as_view(), name='services'),
    path('services/<int:pk>', MedicalServiceRetrieveView.as_view(), name='services-retrieve'),
    ]