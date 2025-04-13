from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.models import User, Group

from rolepermissions.roles import assign_role
from rolepermissions.checkers import has_role



class FiltroForm(forms.Form):
    STATUS_CHOICES = [
        ('O', 'Orçamento'), 
        ('A', 'Aprovado'),
        ('E', 'Executado'),         
        ('V', 'Vistoriado'),
        ('F', 'Finalizado'),
        ('R', 'Rejeitado'), 
    ]

    selected_option = forms.ChoiceField(
        choices=STATUS_CHOICES, 
        widget=forms.RadioSelect(attrs={'class': 'form-control', 'style': 'width: 200px;'}),
        label="Status do Ticket"
    )

    # Obtenha todos os usuários da base de dados
    usuarios = User.objects.all()

   # Criar uma lista de tuplas no formato (id, username) para os usuários
    CHOICES_USER = [("", "Escolha um usuário")] + [(usuario.id, usuario.username) for usuario in usuarios]
    
    
    selected_option_user = forms.ChoiceField(
        choices=CHOICES_USER,
        required=False,  
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 200px;'}),
        label=""
    )
 

    create_date = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date','style': 'width: 200px;'}),
        label="Data de Criação"
    )

    start_date = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date','style': 'width: 200px;'}),
        label="Data inicial"
    )

    end_date = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date', 'style': 'width: 200px;'}),
        label="Data final"
    )

    
