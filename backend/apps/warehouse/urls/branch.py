from django.urls import path
from apps.warehouse.views.branches import income, transfers

app_name = 'warehouse_branch'

urlpatterns = [
    path('income/', income.branch_income_view, name='income-list'),
    path('income/detailed/<int:pk>', income.detailed_income_view, name='income-detailed'),

    path('transfers/', transfers.transfers_view, name='transfers-list'),
    path('transfers/create', transfers.TransferCreate.as_view(), name='transfer-create'),
    path('transfers/update/<int:pk>', transfers.TransferUpdate.as_view(), name='transfer-update'),
    path('transfers/detailed/<int:pk>', transfers.transfers_detailed_view, name='transfers-detailed'),
]
