from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.list_payment, name='list_payment'),
    path('adicionar/', views.add_payment, name='add_payment'),
    path('editar/<int:id_payment>/', views.edit_payment, name='edit_payment'),
    path('excluir/<int:id_payment>/', views.delete_payment, name='delete_payment'),
]