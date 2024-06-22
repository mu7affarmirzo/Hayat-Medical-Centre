from django.urls import path
from apps.warehouse.views.v2 import auth, main_point_income, test, items, income, transfers

app_name = 'warehouse_v2'

urlpatterns = [
    path('login/', auth.login_view, name='login'),
    path('items/', items.get_items, name='items'),
    path('items-search/', items.search_items, name='items-search'),

    path('main_screen/', main_point_income.main_screen_view, name='mainscreen'),

    path('items/items-list', items.items_list_view, name='items-list'),

    # INCOME PATHS
    path('main-point/income/', income.income_view, name='mp-income'),
    path('main-point/income/create', income.ProductCreate.as_view(), name='income-create'),
    path('main-point/income/update/test/<int:pk>', income.ProductUpdate.as_view(), name='income-update-test'),
    path('main-point/income/companies', income.load_delivery_companies, name='load-companies'),
    path('main-point/income/detailed/<int:pk>', income.income_detailed_view, name='mp-income-detailed'),
    # INCOMES ENDS HERE

    path('main-point/cheque/', main_point_income.cheque_view, name='cheque'),
    path('main-point/cheque/detailed/<int:pk>', main_point_income.cheque_detailed_view, name='cheque-detailed'),

    path('main-point/income/xxx', main_point_income.search_items, name='mp-items'),
    path('main-point/item-list/', main_point_income.item_list, name='mp-item-list'),
    path('main-point/register-income/', test.register_income, name='mp-income-register'),
    path('main-point/register-income/dynamic', test.register_income_dynamic, name='mp-income-register-dynamic'),
    path('main-point/item-search/', test.item_search, name='mp-item-search'),

    # TRANSFERS PATHs
    path('main-point/transfers', transfers.transfers_view, name='transfers'),
    path('main-point/transfers/detailed/<int:pk>', transfers.transfers_detailed_view, name='transfers-detailed'),
    path('main-point/transfers/create', transfers.TransferCreate.as_view(), name='transfer-create'),
    path('main-point/transfers/update/<int:pk>', transfers.TransferUpdate.as_view(), name='transfer-update'),
    # TRANSFERS END HERE

]
