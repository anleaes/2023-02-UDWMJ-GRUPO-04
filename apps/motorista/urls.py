from django.urls import path
from . import views

app_name = 'motorista'

urlpatterns = [
    path('', views.list_motoristas, name='list_motoristas'),
    path('adicionar/', views.add_motorista, name='add_motorista'),
    path('editar/<int:id_motorista>/', views.edit_motorista, name='edit_motorista'),
    path('excluir/<int:id_motorista>/', views.delete_motorista, name='delete_motorista'),
]