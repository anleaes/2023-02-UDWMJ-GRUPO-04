from django.urls import path
from . import views

app_name = 'reserve'

urlpatterns = [
    path('', views.list_reserve, name='list_reserve'),
    path('adicionar/<int:id_clients>/', views.add_reserve, name='add_reserve'),
    path('excluir/<int:id_reserve>/', views.delete_reserve, name='delete_reserve'),
    path('excluir-item/<int:id_reserve_item>/', views.delete_reserve_item, name='delete_reserve_item'),
    path('adicionar-item/<int:id_reserve>/', views.add_reserve_item, name='add_reserve_item'),
    path('editar-status/<int:id_reserve>/', views.edit_reserve_status, name='edit_reserve_status'),
]