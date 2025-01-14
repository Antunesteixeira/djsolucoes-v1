from django import forms

from .models import Colaborador

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nomeCol', 'funcao', 'telefone', 'cpf_cnpj', 'pix', 'banco', 'enderecoCol']
        labels = {
            'nomeCol': 'Nome', 
            'funcao': 'Função',
            'telefone': 'Telefone', 
            'cpf_cnpj': 'CPF/CNPJ', 
            'pix': 'Chave Pix',
            'banco': 'Banco',
            'enderecoCol': 'Endereço'
        }

        widgets = {
            'nomeCol': forms.TextInput(attrs={'class': 'form-control','style': 'width: 700px;', 'placeholder':'Exemplo: Antônio José da Silva'}),
            'funcao': forms.TextInput(attrs={'class': 'form-control','style': 'width: 700px;','placeholder':'Exemplo: Eletricista'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control','style': 'width: 700px;','placeholder':'Exemplo: 99 999999999'}),
            'cpf_cnpj': forms.TextInput(attrs={'class': 'form-control','style': 'width: 700px;', 'placeholder':'Digite o CPF ou CNPJ'}),
            'pix': forms.TextInput(attrs={'class': 'form-control','style': 'width: 700px;', 'placeholder':'Coloque a chave pix do colaborador'}),
            'banco': forms.TextInput(attrs={'class': 'form-control','style': 'width: 700px;', 'placeholder':'Exemplo: Bradesco'}),
            'enderecoCol': forms.Textarea(attrs={'class': 'form-control','style': 'width: 700px;', 'rows': 2, 'placeholder':'Avenida Getúlio Vargas, 198, Centro, Magalhães de Aleida - MA'}),
        }