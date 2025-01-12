from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboardCliente, name='dashboard-cliente'),
    path('add-cleinte/', views.addCliente, name='add-cliente'),
    path('editar-cliente/<int:id_cliente>', views.editarCliente, name='editar-cliente'),
    path('deletar-cliente/<int:id_cliente>', views.deletarCliente, name='deletar-cliente'),
]
