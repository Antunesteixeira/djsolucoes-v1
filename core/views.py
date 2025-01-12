from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from rolepermissions.checkers import has_role
from django.contrib.auth.models import User

from ticket.models import Ticket

from django.shortcuts import render

@login_required
def dashboardviews(request):
    usuario = request.user
    if has_role(usuario, [User, 'super']):
        tickets = Ticket.objects.filter(finalizado=False).order_by('-data_criacao')
    else: 
        tickets = Ticket.objects.filter(finalizado=False, usuario=usuario.pk).order_by('-data_criacao')
    context = {
        'tickets': tickets,
        'title': 'Painel',
    }

    return render(request, "index.html", context)

