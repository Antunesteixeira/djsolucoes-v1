from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboardTicket, name='dashboard-ticket'),
    path('add-ticket', views.addTicket, name='add-ticket'),
    path('add-ticket-colaborador/<int:id_ticket>', views.addTicketColaborador, name='add-ticket-colaborador'),
    path('cadastrar-ticket-colaborador/<int:id_colaborador>/<int:id_ticket>', views.cadastrarTicket, name='cadastrar-ticket-colaborador'),
    path('add-ticket-cliente/<int:id_ticket>', views.addTicketCliente, name='add-ticket-cliente'),
    path('cadastrar-ticket-colaborador/<int:id_colaborador>/<int:id_ticket>', views.cadastrarTicket, name='cadastrar-ticket-colaborador'),
    path('cadastrar-ticket-cliente/<int:id_cliente>/<int:id_ticket>', views.cadastrarTicketCliente, name='cadastrar-ticket-cliente'),
    path('ticket/<int:id_ticket>', views.exibirticket, name="ticket"),
    path('editar-ticket/<int:id_ticket>', views.editarTicketViews, name='editar-ticket'),
    path('deletar-ticket/<int:id_ticket>', views.deletarTicketViews, name='deletar-ticket'),
]
