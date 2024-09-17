from django.urls import path
from apps.warehouse.views.headquerter import cheque, expanses, items, transfers, income
from apps.warehouse.views import auth, emergency

app_name = 'warehouse_v2'

urlpatterns = [
    path('login/', auth.login_view, name='login'),
    path('logout/', auth.logout_view, name='logout'),
    path('notification_redirect_view/<int:pk>', auth.notification_redirect_view, name='note_redirect'),

    path('main_screen/', auth.main_screen_view, name='main_screen'),

    # ITEMS PATHS
    path('items-search/', items.item_search, name='mp-item-search'),
    path('items-in-stock-search/', items.items_in_stock_search, name='in-stock-search'),
    path('items/items-list', items.items_list_view, name='items-list'),
    path('items/add-item-to-cheque', cheque.add_item_to_cheque, name='add-item-cheque'),
    # ITEMS END HERE

    # EMERGENCY PATHS
    path('emergency/', emergency.emergency_items_view, name='emergency'),
    # EMERGENCY END HERE

    path('main-point/income/', income.income_view, name='mp-income'),
    path('main-point/income/create', income.ProductCreate.as_view(), name='income-create'),
    path('main-point/income/update/<int:pk>', income.ProductUpdate.as_view(), name='income-update'),
    path('main-point/income/detailed/<int:pk>', income.income_detailed_view, name='mp-income-detailed'),
    # INCOMES ENDS HERE

    # EXPANSES PATHS
    path('main-point/expanses/', expanses.expanses_view, name='expanses'),
    path('main-point/expanses/create', expanses.ExpanseCreate.as_view(), name='expanses-create'),
    path('main-point/expanses/update/<int:pk>', expanses.ExpanseUpdate.as_view(), name='expanses-update'),
    path('main-point/expanses/detailed/<int:pk>', expanses.expanses_detailed_view, name='expanses-detailed'),
    # EXPANSES ENDS HERE

    # CHEQUE PATHS
    path('main-point/cheque/', cheque.cheque_view, name='cheque'),
    path('main-point/cheque/create', cheque.ChequeCreate.as_view(), name='cheque-create'),
    path('main-point/cheque/update/<int:pk>', cheque.ChequeUpdate.as_view(), name='cheque-update'),
    path('main-point/cheque/detailed/<int:pk>', cheque.cheque_detailed_view, name='cheque-detailed'),
    path('main-point/cheque/add-new-patient', cheque.add_new_patient, name='add-new-patient'),

    path('main-point/cheque/invoice/<int:pk>', cheque.gen_invoice, name='invoice-gen'),
    # CHEQUE ENDS HERE

    # TRANSFERS PATHs
    path('main-point/transfers', transfers.transfers_view, name='transfers'),
    path('main-point/transfers/detailed/<int:pk>', transfers.transfers_detailed_view, name='transfers-detailed'),
    path('main-point/transfers/create', transfers.TransferCreate.as_view(), name='transfer-create'),
    path('main-point/transfers/update/<int:pk>', transfers.TransferUpdate.as_view(), name='transfer-update'),
    # TRANSFERS END HERE

]
