from django.urls import path
from . import views

app_name = 'reservas'

urlpatterns = [
    path('', views.list_reservas, name='list_orders'),
    path('adicionar/<int:id_client>/', views.add_reservas, name='add_reservas'),
    path('excluir/<int:id_reservas>/', views.delete_reservas, name='delete_reservas'),
    path('excluir-item/<int:id_reservas_item>/', views.delete_reservas_item, name='delete_reservas_item'),
    path('adicionar-item/<int:id_reservas>/', views.add_reservas_item, name='add_reservas_item'),
    path('editar-status/<int:id_reservas>/', views.edit_reservas_status, name='edit_reservas_status'),
]