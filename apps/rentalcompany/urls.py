from django.urls import path
from . import views

app_name = 'rentalcompany'

urlpatterns = [
    path('', views.list_products, name='list_rentalcompanys'),
    path('adicionar/', views.add_product, name='add_rentalcompany'),
    path('editar/<int:id_product>/', views.edit_product, name='edit_rentalcompany'),
    path('excluir/<int:id_product>/', views.delete_product, name='delete_rentalcompany'),
]
