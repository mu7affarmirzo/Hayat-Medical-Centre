from django.urls import path
from apps.warehouse.views.branches import income

app_name = 'warehouse_branch'

urlpatterns = [
    path('income/', income.branch_income_view, name='income-list'),
    path('income/detailed/<int:pk>', income.detailed_income_view, name='income-detailed'),
]
