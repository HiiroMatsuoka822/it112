from django.urls import path
from . import views

urlpatterns = [
    path('api/items/', views.get_all_items, name='get_all_items'),
    path('api/item/', views.get_single_item, name='get_single_item'),
    path('api/create_item/', views.create_item, name='create_item'),
]