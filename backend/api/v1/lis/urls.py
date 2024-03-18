from django.urls import path, include
from api.v1.lis.views.labs import LabResearchCategoryListAPIView

app_name = 'lis'

urlpatterns = [
    path('get_labs_group_by_category/', LabResearchCategoryListAPIView.as_view(), name='labs'),
]
