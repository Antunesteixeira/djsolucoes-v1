
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib import messages
from rolepermissions.checkers import has_role

from django.contrib.auth.decorators import login_required

from ticket.models import Ticket

from .models import Cliente
from .forms import ClienteForm

@login_required
def dashboardCliente(request):
    usuario = request.user
    if has_role(usuario, [User, 'super']):
        clientes = Cliente.objects.filter(usuario=usuario)
    else:
        clientes = Cliente.objects.filter(usuario=request.user.pk)

    context = {
        'clientes':clientes,
        'title':'Listar Clientes',
    }
    return render(request, 'cliente/index-cliente.html', context)

@login_required
def addCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            messages.add_message(request, messages.SUCCESS, "Cliente cadastrado com sucesso!")
            return redirect('/cliente/')
    else:    
        form = ClienteForm()
    
    context = {
        'form': form, 
        'title':'Cadastrar Cliente'
    }

    return render(request, 'crud/cadastrar.html', context)

@login_required
def editarCliente(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Cliente editado com sucesso!")
        return redirect('/cliente/')
    
    context = {
        'cliente':cliente, 
        'form':form,
        'url': 'cliente',
        'title': 'Editar Cliente',
        'id':id_cliente
    }

    return render(request, 'crud/editar.html', context)

@login_required
def deletarCliente(request, id_cliente):
    ticket = Ticket.objects.filter(cliente=id_cliente)
    if ticket:
        messages.add_message(request, messages.ERROR, f"O Cliente não pode ser deletado, pois está associado a um ou mais tickets!")
    else:
        cliente = Cliente.objects.get(pk=id_cliente).delete()
        messages.add_message(request, messages.ERROR, "Cliente deletado com sucesso!")
    
    return redirect('/cliente/')