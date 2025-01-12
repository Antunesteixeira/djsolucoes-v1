from django import forms

from .models import Colaborador

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nomeCol', 'funcao', 'cpf_cnpj', 'pix', 'enderecoCol']
        labels = {
            'nomeCol': 'Nome', 
            'funcao': 'Função', 
            'cpf_cnpj': 'CPF/CNPJ', 
            'pix': 'Chave Pix',
            'enderecoCol': 'Endereço'
        }

        widgets = {
            'nomeCol': forms.TextInput(attrs={'class': 'form-control','style': 'width: 700px;', 'placeholder':'Exemplo: Antônio José da Silva'}),
            'funcao': forms.TextInput(attrs={'class': 'form-control','style': 'width: 700px;','placeholder':'Exemplo: Eletricista'}),
            'cpf_cnpj': forms.TextInput(attrs={'class': 'form-control','style': 'width: 700px;', 'placeholder':'Digite o CPF ou CNPJ'}),
            'pix': forms.TextInput(attrs={'class': 'form-control','style': 'width: 700px;', 'placeholder':'Coloque a chave pix do colaborador'}),
            'enderecoCol': forms.Textarea(attrs={'class': 'form-control','style': 'width: 700px;', 'rows': 2, 'placeholder':'Avenida Getúlio Vargas, 198, Centro, Magalhães de Aleida - MA'}),
        }