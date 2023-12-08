from django.urls import path
from . import views

app_name = 'rentalcompany'

urlpatterns = [
    path('', views.list_rentalcompany, name='list_rentalcompany'),
    path('adicionar/', views.add_rentalcompany, name='add_rentalcompany'),
    path('editar/<int:id_rentalcompany>/', views.edit_rentalcompany, name='edit_rentalcompany'),
    path('excluir/<int:id_rentalcompany>/', views.delete_rentalcompany, name='delete_rentalcompany'),
]
