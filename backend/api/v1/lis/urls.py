from django.urls import path, include
from api.v1.lis.views.labs import LabResearchCategoryListAPIView, get_list_research

app_name = 'lis'

urlpatterns = [
    path('get_labs_group_by_category/', LabResearchCategoryListAPIView.as_view(), name='labs'),
    path('get_list_category/', LabResearchCategoryListAPIView.as_view(), name='labs'),
    path('research/get_list_research/', get_list_research, name='labs'),
]

