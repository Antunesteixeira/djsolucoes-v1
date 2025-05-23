from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib import messages
from rolepermissions.checkers import has_role

from django import forms

from django.contrib.auth.decorators import login_required

from .models import Ticket
from colaborador.models import Colaborador
from cliente.models import Cliente
from .forms import TicketForm

from django.shortcuts import render

from datetime import datetime

@login_required
def dashboardTicket(request):
    usuario = request.user
    if has_role(usuario, [User, 'super']):
        tickets = Ticket.objects.all().order_by('-data_criacao')        
    else: 
        tickets = Ticket.objects.filter(usuario=usuario.pk).order_by('-data_criacao')
    context = {
        'tickets':tickets,
        'title': 'Tickets',
    }
    return render(request, 'ticket/index-ticket.html', context)

@login_required
def addTicket(request):
    tickets = Ticket.objects.all()

    if request.method == 'POST':
        ticket = TicketForm(request.POST)
        
        # Verificar se o formulário é válido
        if ticket.is_valid():
            # Acessar os dados validados após o formulário ser válido
            ticket_number = ticket.cleaned_data['ticket']
            
            # Verificar se o ticket já existe
            existe = Ticket.objects.filter(ticket=ticket_number).exists()
            if existe:
                messages.add_message(request, messages.WARNING, "O número do Ticket já existe!")
                return redirect('/ticket/add-ticket')
            
            # Se o ticket não existir, salvar o novo ticket
            obj = ticket.save(commit=False)
            obj.usuario = request.user
            obj.save()
            messages.add_message(request, messages.SUCCESS, "Ticket cadastrado! Deseja vincular um colaborador agora?")
            return redirect(f'/ticket/add-ticket-colaborador/{obj.pk}')
        else:
            # Se o formulário não for válido
            messages.add_message(request, messages.ERROR, "Erro ao cadastrar ticket! Verifique as informações de ticket!")
            return redirect('/ticket/add-ticket')

    form = TicketForm()
    form.fields['emergencial'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
    context = {
        'form': form,
        'title':'Cadastrar Ticket'
    }


    return render(request, 'ticket/add-ticket.html', context)

@login_required
def addTicketColaborador(request, id_ticket):
    usuario = request.user
    if request.method == 'GET':
        if has_role(usuario, [User, 'super']):
            colaboradores = Colaborador.objects.all()
        else:
            colaboradores = Colaborador.objects.filter(usuario=usuario.pk)

    origem = request.GET.get('origem', None)

    context = {
        'colaboradores':colaboradores, 
        'id_ticket':id_ticket,
        'title': 'Adicionar Colaborador ao Ticket',
        'origem': origem,
    }
    return render(request, 'ticket/add-ticket-colaborador.html', context)

@login_required
def cadastrarTicket(request, id_colaborador, id_ticket):
    if request.method == 'GET':
        # Obtém o ticket ou retorna 404 se não existir
        ticket = get_object_or_404(Ticket, id=id_ticket)
        
        # Obtém o colaborador ou retorna 404 se não existir
        col = get_object_or_404(Colaborador, id=id_colaborador)

        # Associa o colaborador ao ticket
        ticket.colaborador = col
        ticket.save()
    
        messages.add_message(request, messages.INFO, f"O Colaborador: {ticket.colaborador} foi adicionado ao Ticket: {ticket.ticket} com sucesso!")
        #return HttpResponse(request.POST['editar-colaborador'] == 'editar-colaborador')
        
        origem = request.GET['origem']
        if origem == 'link-colaborador':
            return redirect('/ticket/')
        else:
            return redirect(f'/ticket/add-ticket-cliente/{id_ticket}')

@login_required    
def addTicketCliente(request, id_ticket):
    usuario = request.user
    if request.method == 'GET':
        if has_role(usuario, [User, 'super']):
            clientes = Cliente.objects.all()
        else:
            clientes = Cliente.objects.filter(usuario=usuario)    
    
    return render(request, 'ticket/add-ticket-cliente.html', {'clientes':clientes, 'id_ticket':id_ticket})

@login_required
def cadastrarTicketCliente(request, id_cliente, id_ticket):
    if request.method == 'GET':
        # Obtém o ticket ou retorna 404 se não existir
        ticket = get_object_or_404(Ticket, id=id_ticket)
        
        # Obtém o cliente ou retorna 404 se não existir
        cli = get_object_or_404(Cliente, id=id_cliente)

        # Associa o clinete ao ticket
        ticket.cliente = cli
        ticket.save()
    
        messages.add_message(request, messages.INFO, f"O Clinete: {ticket.cliente} foi adicionado ao Ticket: {ticket.ticket} com sucesso!")

        return redirect('/ticket/')
    
@login_required    
def exibirticket(request, id_ticket):
    ticket = get_object_or_404(Ticket, id=id_ticket)
    valor_custo_total = ticket.func_valor_custo_total()
    bdi = ticket.func_bdi()
    context = {
        'ticket':ticket,
        'valor_custo_total':valor_custo_total,
        'bdi': bdi,
    }
    return render(request, 'ticket/ticket.html', context)

@login_required  
def editarTicketViews(request, id_ticket):
    ticket = Ticket.objects.get(pk=id_ticket)
    form = TicketForm(request.POST or None, instance=ticket)

    if request.user.is_superuser:
        form.fields['emergencial'].widget = forms.CheckboxInput()  # Ou o widget que você preferir
    else:
        form.fields['emergencial'].widget = forms.HiddenInput()

    if form.is_valid():
        finalizado = ticket.func_finalizado()
        ticket.ultimo_update = datetime.now()
        form.save()
        messages.add_message(request, messages.SUCCESS, "Ticket alterado com sucesso!")
        return redirect('/ticket/', messages)

    return render(request, 'ticket/editar-ticket.html', {'ticket':ticket, 'form':form})

@login_required
def deletarTicketViews(request, id_ticket):
    ticket = get_object_or_404(Ticket, pk=id_ticket)
    ticket.delete()
    messages.success(request, "Ticket deletado com sucesso!")
    return redirect('/ticket/')