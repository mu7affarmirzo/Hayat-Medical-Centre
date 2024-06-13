from django.urls import path

from api.v1.lis.views.labs import LabResearchCategoryListAPIView, get_list_research
from api.v1.lis.views.orders import get_list_ordered_researches, update_test_container_code_view, \
    validate_ordered_research_view, validate_ordered_research_choices

app_name = 'lis'

urlpatterns = [
    path('get_labs_group_by_category/', LabResearchCategoryListAPIView.as_view(), name='labs'),
    path('get_list_category/', LabResearchCategoryListAPIView.as_view(), name='labs'),
    path('research/get_list_research/', get_list_research, name='labs'),
    path('orders/get-list-ordered-researches/', get_list_ordered_researches, name='labs'),
    path('orders/get-list-ordered-researches/<int:pk>', get_list_ordered_researches, name='labs'),
    path('orders/update-test-container/<int:pk>', update_test_container_code_view, name='labs'),
    path('orders/validate-research-test/<int:pk>', validate_ordered_research_view, name='labs'),
    path('orders/validate-research-choices', validate_ordered_research_choices, name='labs'),

]
