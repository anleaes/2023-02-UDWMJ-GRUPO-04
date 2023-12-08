from django.urls import path
from . import views

app_name = 'veiculos'

urlpatterns = [
    path('', views.list_veiculos, name='list_veiculos'),
    path('adicionar/', views.add_veiculo, name='add_veiculo'),
    path('editar/<int:id_veiculo>/', views.edit_veiculo, name='edit_veiculo'),
    path('excluir/<int:id_veiculo>/', views.delete_veiculo, name='delete_veiculo'),
]