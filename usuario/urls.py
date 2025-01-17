from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboarUsuario, name="index-usuario"),
    #path('add-usuario/', views.addUsuario, name="add-usuario"),
    path('sair/', views.sairUsuario, name='sair'),
    path('perfil-usuario/<id_usuario>', views.perfilUsuario, name='perfil-usuario'),
    path('criar-usuario/', views.criar_usuario, name='criar-usuario'),
]