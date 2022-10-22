from django.urls import path, include
from api.v1.organizations.views.patient import PatientView, PatientRetrieveView
from api.v1.organizations.views.organizations import OrganizationsListCreateView, BranchesListCreateView
from api.v1.organizations.views.specialties import SpecialtiesView

urlpatterns = [
    # path('account/', include('api.v1.account.urls')),
    path('', OrganizationsListCreateView.as_view(), name='organizations'),
    path('branches/', BranchesListCreateView.as_view(), name='branches'),
    path('specialites/', SpecialtiesView.as_view(), name='specialites'),
    path('patients/', PatientView.as_view(), name='patients'),
    path('patients/<int:pk>', PatientRetrieveView.as_view(), name='patients'),

]