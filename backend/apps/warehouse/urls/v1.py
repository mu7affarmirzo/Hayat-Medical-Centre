# from django.urls import path
# from apps.warehouse.views import *
# from apps.warehouse.views.old import main
#
# app_name = 'warehouse'
#
# urlpatterns = [
#     path('login/', main.login_view, name='warehouse-login'),
#     path('logout/', main.logout_view, name='warehouse-logout'),
#     path('index/', main.index_view, name='warehouse-index'),
#
#     path('rec-reg/', main.receive_registry_view, name='warehouse-recreg'),
#     path('rec-reg/<int:pk>', main.receive_registry_view, name='warehouse-recreg'),
#
#     path('send-reg-create/', create_send_reg_view, name='warehouse-create-send-reg'),
#     path('send-reg-create/<int:s_pk>', get_send_reg_view, name='warehouse-create-send-reg'),
#     path('send-reg-popup-post/<int:s_pk>', send_reg_popup_post, name='send-reg-popup-post'),
#     path('send-reg-popup-insurance-post/<int:s_pk>', send_reg_popup_insurance_post,
#          name='send-reg-popup-insurance-post'),
#
#     path('medicines/', main.medicines_view, name='warehouse-medicines'),
#     path('medicines/<int:pk>', main.medicines_view, name='warehouse-medicines'),
#     path('cheque/', create_cheque_view, name='cheque-create'),
#     path('cheque/<int:pk>', get_cheque_view, name='cheque-get'),
#     path('cheque/<int:ch_pk>/<int:i_pk>', add_item_to_cheque_view, name='cheque-item-add'),
#     path('cheque-pdf/<int:pk>', cheque_save_pdf, name='cheque-pdf'),
#     path('incomes/', receive_registry_view, name='warehouse-incomes'),
#     path('incomes/<int:pk>', receive_registry_view, name='warehouse-incomes'),
#
#     path('cheque-popup/<int:pk>', cheque_popup_view, name='cheque-popup'),
#     path('cheque-popup-post/<int:ch_pk>', cheque_popup_post, name='cheque-popup-post'),
#     path('cheque-popup-insurance-post/<int:ch_pk>', cheque_popup_insurance_post, name='cheque-popup-insurance-post'),
#
#     path('expense/', create_expense_view, name='expense-create'),
#     path('expense/<int:e_pk>', get_expense_view, name='expense-get'),
#     path('delete-expense/<int:e_pk>', delete_expense, name='delete-expense'),
#     path('expense-popup-post/<int:e_pk>', expense_popup_post, name='expense-popup-post'),
#     path('expense-popup-insurance-post/<int:e_pk>', expense_popup_insurance_post, name='expense-popup-insurance-post'),
#
#     path('items/', items_list, name='items-list'),
#     path('items/<int:pk>', item_history, name='item-history'),
#     path('item-post/', post_item, name='item-post'),
# ]
