from django.urls import path, include

from api.v1.doctors.views.medical_service import MedicalServiceView, MedicalServiceRetrieveView
from api.v1.organizations.views.branches import specialty_by_branch_view, get_specialty_by_id_view, \
    doctors_by_branch_view
from api.v1.organizations.views.doctors import DoctorsListCreateView, DoctorsRetrieveView
from api.v1.organizations.views.patient import PatientView, PatientRetrieveView, PatientFilterView
from api.v1.organizations.views.organizations import OrganizationsListCreateView, BranchesListCreateView
from api.v1.organizations.views.specialties import SpecialtiesView, DoctorSpecialitiesView
from api.v1.organizations.views.patient_group import *


urlpatterns = [
    path('', OrganizationsListCreateView.as_view(), name='organizations'),
    path('branches/', BranchesListCreateView.as_view(), name='branches'),
    path('branches/specialty/<int:pk>', specialty_by_branch_view, name='branch-spec'),
    path('branches/specialty/<int:pk>/<int:spec_id>', get_specialty_by_id_view, name='branch-spec'),

    path('branches/doctors/<int:branch_id>', doctors_by_branch_view, name='branch-docs'),

    path('specialities/', SpecialtiesView.as_view(), name='specialites'),

    path('patients/', PatientView.as_view(), name='patients'),
    path('patients-search/', PatientFilterView.as_view(), name='patients-search'),
    path('patients/<int:pk>', PatientRetrieveView.as_view(), name='patients'),

    path('doctors/', DoctorsListCreateView.as_view(), name='doctors'),
    path('doctors/<int:pk>', DoctorsRetrieveView.as_view(), name='doctors'),

    path('doc-specialities/', DoctorSpecialitiesView.as_view(), name='doctors-specialities'),

    path('patient-group/', PatientGroupView.as_view(), name='patient-group'),
    path('patient-group/<int:pk>', PatientGroupRetrieveView.as_view(), name='patient-group'),

]


