from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group

class UsuarioForm(UserCreationForm):
    grupo = forms.ModelChoiceField(
        queryset=Group.objects.all(),  # Lista todos os grupos
        required=True,  # Torna o campo obrigatório
        label="Grupo"
    )
    email = forms.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'grupo']

    def save(self, commit=True):
        # Salva o usuário e adiciona ao grupo selecionado
        user = super().save(commit=False)
        group = self.cleaned_data['grupo']  # Obtém o grupo selecionado

        if commit:
            user.save()
            user.groups.add(group)  # Adiciona o usuário ao grupo

        return user