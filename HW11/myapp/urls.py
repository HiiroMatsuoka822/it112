# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Route for fetching all items: /api/items/all
    path('api/items/all/', views.get_all_items, name='get_all_items'),
    # Route for fetching a single item: /api/items/single/?id=<item_id>
    path('api/items/single/', views.get_single_item, name='get_single_item'),
    # Route for adding a new item via POST: /api/items/add/
    path('api/items/add/', views.add_item, name='add_item'),
]