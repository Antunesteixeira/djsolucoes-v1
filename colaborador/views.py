from django.shortcuts import render, redirect
from django.contrib import messages
from rolepermissions.checkers import has_role
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from ticket.models import Ticket

from .forms import ColaboradorForm
from .models import Colaborador

@login_required
def dashboardcolaborador(request):
    usuario = request.user
    if has_role(usuario, [User, 'super']):
        colaboradores = Colaborador.objects.all()
    else:
        colaboradores = Colaborador.objects.filter(usuario=usuario)
        
    context = {
        'colaboradores':colaboradores,
        'title':'Listar Colaborador'
    }    
    return render(request, 'colaborador/index-colaborador.html', context)

@login_required
def addColaborador(request):
    form = ColaboradorForm()
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            messages.add_message(request, messages.SUCCESS, "Colaborador cadastrado com sucesso!")
            return redirect('/colaborador/', messages)
    else:    
        form = ColaboradorForm()

    context = {
        'title': 'Cadastrar Colaborador',
        'form': form        
    }

    return render(request, 'crud/cadastrar.html', context)
    
@login_required
def editarColaborador(request, id_colaborador):
    colaborador = Colaborador.objects.get(pk=id_colaborador)
    form = ColaboradorForm(request.POST or None, instance=colaborador)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Colaborador editado, com sucesso!")
        return redirect('/colaborador/')
    
    context = {
        'colaborador':colaborador, 
        'form':form,
        'url': 'colaborador',
        'title': 'Editar Colaborador',
        'id': id_colaborador,
    }

    return render(request, 'crud/editar.html', context)

@login_required
def deletarColaborador(request, id_colaborador):
    ticket = Ticket.objects.filter(cliente=id_colaborador)
    if ticket:
        messages.add_message(request, messages.ERROR, f"O Colaborador não pode ser deletado, pois está associado a um ou mais tickets!")
    else:
        colaborador = Colaborador.objects.get(pk=id_colaborador).delete()
        messages.add_message(request, messages.ERROR, "Colaborador deletado com sucesso!")

    return redirect('/colaborador/')
    
        
