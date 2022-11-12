import django_filters as filters
from django.db.models import F, Case, When, BooleanField
from apps.account.models.patients import PatientModel


class PatientFilter(filters.FilterSet):

    class Meta:
        model = PatientModel
        fields = [
            'l_name',
            'f_name',
            'mid_name',
            'INN',
            'doc_number',
            'date_of_birth',
            'mobile_phone_number',
            'id',
            'last_visit_at',
        ]