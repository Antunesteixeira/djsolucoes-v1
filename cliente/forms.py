from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'gerente_loja', 'telefone', 'gerente_regional', 'enderecoCli']
        labels = {
            'nome': 'Nome Completo',
            'gerente_loja': 'Gerente',
            'gerente_regional': 'Gerente Regional',
            'enderecoCli': 'Endereço'
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control','style': 'width: 700px;', 'placeholder':'Nome Completo'}),
            'gerente_loja': forms.TextInput(attrs={'class': 'form-control','style': 'width: 700px;','placeholder':'Informe o nome do gerente da loja'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control','style': 'width: 700px;', 'placeholder':'Exemplo? (98) 99999999'}),
            'gerente_regional': forms.TextInput(attrs={'class': 'form-control','style': 'width: 700px;', 'placeholder':'nforme o nome do gerente regional'}),
            'enderecoCli': forms.Textarea(attrs={'class': 'form-control','style': 'width: 700px;', 'rows': 2, 'placeholder':'Avenida Getúlio Vargas, 198, Centro, Magalhães de Aleida - MA'}),
        }