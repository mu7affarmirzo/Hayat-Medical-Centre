from django.urls import path, include


urlpatterns = [
    path('', include('apps.sanatorium.routers.auth')),
    path('staff/', include('apps.sanatorium.routers.staff')),
    path('doctors/', include('apps.sanatorium.routers.doctors')),
    path('nurses/', include('apps.sanatorium.routers.nurses')),
    path('dispatchers/', include('apps.sanatorium.routers.dispatcher')),
    path('procedure_specs/', include('apps.sanatorium.routers.procedure_specs')),
]


