from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'), 
    path('add/', views.add_item, name='add'),    # Add new item
    path('edit/<int:item_id>/', views.item_edit, name='item_edit'),  # Edit
    path('delete/<int:item_id>/', views.item_delete, name='item_delete'),  # Delete
]



