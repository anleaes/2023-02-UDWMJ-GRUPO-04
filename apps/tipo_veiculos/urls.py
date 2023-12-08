from django.urls import path
from . import views

app_name = 'tipo_veiculos'

urlpatterns = [
    path('', views.list_tipo_veiculos, name='list_tipo_veiculos'),
    path('adicionar/', views.add_tipoveiculos, name='add_tipoveiculos'),
    path('excluir/<int:id_tipoveiculos>/', views.delete_tipoveiculos, name='delete_tipoveiculos'),
]