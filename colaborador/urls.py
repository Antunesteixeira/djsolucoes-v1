from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboardcolaborador, name="dashboard-colaborador"),
    path('add-colaborador/', views.addColaborador, name="add-colaborador"),
    path('editar-colaborador/<int:id_colaborador>', views.editarColaborador, name='editar-colaborador'),
    path('deletar-colaborador/<int:id_colaborador>', views.deletarColaborador, name='deletar-colaborador'),
]