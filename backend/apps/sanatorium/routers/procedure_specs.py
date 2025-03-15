from django.urls import path, include

from apps.sanatorium.views import procedure_specs

app_name = 'sanatorium_procedure_specs'


urlpatterns = [
    path('procedures/', procedure_specs.get_assigned_procedures, name='main_screen'),
    path('get-procedures-by-date/', procedure_specs.get_procedures_by_start_date_view, name='get-procedures-by-date'),
    path('get-all-procedures/', procedure_specs.get_all_procedures, name='all_procedures'),
    path('update-procedure-state/<int:pk>', procedure_specs.update_procedure_state_view, name='update_procedure_state'),
    path('make-it-done-procedure-state/<int:pk>', procedure_specs.make_it_done_procedure_state_view, name='make_it_done_procedure_state'),

]

