from django.urls import path
from apps.warehouse.views.v2 import auth, items
from apps.warehouse.views.v2 import auth, main_point_income, test, items

app_name = 'warehouse_v2'

urlpatterns = [
    path('login/', auth.login_view, name='v2-login'),
    path('items/', items.get_items, name='v2-items'),
    path('items-search/', items.search_items, name='v2-items-search'),
    path('main_screen/', main_point_income.main_screen_view, name='v2-mainscreen'),
    path('items/items-list', items.items_list_view, name='v2-items-list'),

    path('main-point/income/', main_point_income.income_view, name='v2-mp-income'),
    path('main-point/income/create', main_point_income.income_create_view, name='v2-mp-income-create'),
    path('main-point/income/detailed/<int:pk>', main_point_income.income_detailed_view, name='v2-mp-income-detailed'),

    path('main-point/cheque/', main_point_income.cheque_view, name='cheque'),
    path('main-point/cheque/detailed/<int:pk>', main_point_income.cheque_detailed_view, name='cheque-detailed'),

    path('main-point/income/', main_point_income.search_items, name='v2-mp-items'),
    path('main-point/item-list/', main_point_income.item_list, name='v2-mp-item-list'),
    path('main-point/register-income/', test.register_income, name='v2-mp-income-register'),
    path('main-point/item-search/', test.item_search, name='v2-mp-item-search'),

]
