from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('add/', views.add_item, name='add'),
    path('edit/<int:item_id>/', views.item_edit, name='item_edit'),
    path('delete/<int:item_id>/', views.item_delete, name='item_delete'),
    path('check-serial/', views.check_serial, name='check_serial'),  # AJAX validation
]




