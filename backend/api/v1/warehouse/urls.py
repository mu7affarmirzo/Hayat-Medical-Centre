from django.urls import path
from api.v1.warehouse.views import *

urlpatterns = [
    path('company/', get_company_view),
    path('company/<int:pk>', get_company_retrieve_view),
    path('company-create/', create_company_view),
    path('company-update/<int:pk>', update_company_view),
    path('company-delete/<int:pk>', delete_company_view),

    path('income/', get_income_view),
    path('income/<int:pk>', get_income_retrieve_view),
    path('income-create/', create_income_view),
    path('income-update/<int:pk>', update_income_view),
    path('income-delete/<int:pk>', delete_income_view),

    path('income-items/', get_income_item_view),
    path('income-items/<int:pk>', get_income_item_retrieve_view),
    path('income-items-create/', create_income_item_view),
    path('income-items-update/<int:pk>', update_income_item_view),
    path('income-items-delete/<int:pk>', delete_income_item_view),

    path('items/', get_item_view),
    path('items/<int:pk>', get_item_retrieve_view),
    path('items-create/', create_item_view),
    path('items-update/<int:pk>', update_item_view),
    path('items-delete/<int:pk>', delete_item_view),

    path('items-in-stock/', get_item_in_stock_view),
    path('items-in-stock/<int:pk>', get_item_in_stock_retrieve_view),
    path('items-in-stock-create/', create_item_in_stock_view),
    path('items-in-stock-update/<int:pk>', update_item_in_stock_view),
    path('items-in-stock-delete/<int:pk>', delete_item_in_stock_view),

    path('receive-registry/', get_receive_registry_view),
    path('receive-registry/<int:pk>', get_receive_registry_retrieve_view),
    path('receive-registry-create/', create_receive_registry_view),
    path('receive-registry-update/<int:pk>', update_receive_registry_view),
    path('receive-registry-delete/<int:pk>', delete_receive_registry_view),

    path('received-items/', get_received_item_view),
    path('received-items/<int:pk>', get_received_item_retrieve_view),
    path('received-items-create/', create_received_item_view),
    path('received-items-update/<int:pk>', update_received_item_view),
    path('received-items-delete/<int:pk>', delete_received_item_view),

    path('send-registry/', get_send_registry_view),
    path('send-registry/<int:pk>', get_send_registry_retrieve_view),
    path('send-registry-create/', create_send_registry_view),
    path('send-registry-update/<int:pk>', update_send_registry_view),
    path('send-registry-delete/<int:pk>', delete_send_registry_view),

    path('sent-items/', get_sent_items_view),
    path('sent-items/<int:pk>', get_sent_items_retrieve_view),
    path('sent-items-create/', create_sent_items_view),
    path('sent-items-update/<int:pk>', update_sent_items_view),
    path('sent-items-delete/<int:pk>', delete_sent_items_view),

    path('store-point/', get_store_point_view),
    path('store-point/<int:pk>', get_store_point_retrieve_view),
    path('store-point-create/', create_store_point_view),
    path('store-point-update/<int:pk>', update_store_point_view),
    path('store-point-delete/<int:pk>', delete_store_point_view),

]
