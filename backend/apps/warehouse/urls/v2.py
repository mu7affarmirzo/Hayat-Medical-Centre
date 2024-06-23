from django.urls import path
from apps.warehouse.views import transfers, items, income, main_point_income, auth, cheque

app_name = 'warehouse_v2'

urlpatterns = [
    path('login/', auth.login_view, name='login'),
    path('logout/', auth.logout_view, name='logout'),

    path('main_screen/', main_point_income.main_screen_view, name='mainscreen'),

    # ITEMS PATHS
    path('items-search/', items.item_search, name='mp-item-search'),
    path('items/items-list', items.items_list_view, name='items-list'),
    path('items/items-list', items.items_list_view, name='items-list'),
    # ITEMS END HERE

    path('main-point/income/', income.income_view, name='mp-income'),
    path('main-point/income/create', income.ProductCreate.as_view(), name='income-create'),
    path('main-point/income/update/test/<int:pk>', income.ProductUpdate.as_view(), name='income-update-test'),
    path('main-point/income/companies', income.load_delivery_companies, name='load-companies'),
    path('main-point/income/detailed/<int:pk>', income.income_detailed_view, name='mp-income-detailed'),
    # INCOMES ENDS HERE

    # CHEQUE PATHS
    path('main-point/cheque/', cheque.cheque_view, name='cheque'),
    path('main-point/cheque/detailed/<int:pk>', cheque.cheque_detailed_view, name='cheque-detailed'),
    # CHEQUE ENDS HERE

    # TRANSFERS PATHs
    path('main-point/transfers', transfers.transfers_view, name='transfers'),
    path('main-point/transfers/detailed/<int:pk>', transfers.transfers_detailed_view, name='transfers-detailed'),
    path('main-point/transfers/create', transfers.TransferCreate.as_view(), name='transfer-create'),
    path('main-point/transfers/update/<int:pk>', transfers.TransferUpdate.as_view(), name='transfer-update'),
    # TRANSFERS END HERE

]
