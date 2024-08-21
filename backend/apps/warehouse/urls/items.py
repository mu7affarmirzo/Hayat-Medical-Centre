from django.urls import path
from apps.warehouse.views.manual import items

urlpatterns = [
    path("", items.items_get_view, name="items"),
    path("item-create", items.item_create, name="item-create"),
    path("item-update/<int:pk>", items.item_update, name="item-update"),
    path("item-delete/<int:pk>", items.item_delete, name="item-delete")
]
