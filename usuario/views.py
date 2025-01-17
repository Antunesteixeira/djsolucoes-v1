from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import logout

from django.contrib.auth.models import User

from rolepermissions.roles import assign_role
from rolepermissions.checkers import has_role
from rolepermissions.decorators import has_role_decorator, has_permission_decorator

from django.contrib.auth.decorators import login_required

from .forms import UsuarioForm

@login_required
@has_role_decorator('super')
def dashboarUsuario(request):
    usuarios = User.objects.all()
    context = {
        'title': 'Usuários',
        'usuarios': usuarios
    }
    return render(request, 'usuario/index-usuarios.html', context)

'''
@login_required
@has_role_decorator('super')
def addUsuario(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST['email']
        password = request.POST["password"]
        usuario = User.objects.create_user(username, email, password)
        usuario.save()
        assign_role(usuario, request.POST["nivel"])
        messages.add_message(request, messages.SUCCESS, "Usuário cadastrado com sucesso!")
        return redirect('/usuario/')
    
    else:
        context = {
            'title': 'Cadastro de Usuário'
        }
        return render(request, 'usuario/add-usuario.html', context)
'''
    
@login_required  
def sairUsuario(request):
    logout(request)
    return redirect('/accounts/login')

@login_required
def perfilUsuario(request, id_usuario):
    usuario = User.objects.get(pk=id_usuario)
    context = {
        'usuario':usuario,
        'title': 'Perfil do Usuário',
    }
    return render(request, 'usuario/perfil-usuario.html', context)

def criar_usuario(request):
    form = UsuarioForm(request.POST)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            messages.add_message(request, messages.SUCCESS, "Usuário cadastrado com sucesso!")
            return redirect('/usuarios/')
    else:
        form = UsuarioForm()

    context = {
        'title': 'Criar Usuário',
        'form': form,
    }
    return render(request, 'usuario/form-usuario.html', context)