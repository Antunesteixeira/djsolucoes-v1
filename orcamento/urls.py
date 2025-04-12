from django.urls import path

from . import views

urlpatterns = [
    path('<int:id_ticket>', views.orcamento, name='index-orcamento'),
    path('lista-orcamento/<int:id_orcamento>', views.lista_orcamento, name='lista-orcamento')
]