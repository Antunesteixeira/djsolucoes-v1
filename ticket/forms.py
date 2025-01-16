from django import forms

from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket', 'status', 'emergencial', 'valor_mao_obra', 'valor_custo', 'valor_faturamento', 'data_finalizar', 'descricao']

        labels = {
            'ticket': 'Ticket',            
            'status':'Status',
            'valor_custo': 'Custo de Material',
            'valor_mao_obra': 'Custo Mão de Obra'
        }

        widgets = {
            'ticket': forms.TextInput(attrs={'class': 'form-control','style': 'width: 700px;','placeholder':'nº do ticket'}),
            'emergencial': forms.HiddenInput(attrs={'class': 'form-check-input'}),
            'status': forms.Select(attrs={'class': 'form-control','style': 'width: 200px;'}),
            'valor_mao_obra': forms.TextInput(attrs={'class': 'form-control','style': 'width: 200px;', 'placeholder':'Exemplo: R$ 100,00'}),
            'valor_custo': forms.TextInput(attrs={'class': 'form-control','style': 'width: 200px;', 'placeholder':'Exemplo: R$ 200,00'}),
            'valor_faturamento': forms.TextInput(attrs={'class': 'form-control','style': 'width: 200px;', 'placeholder':'Exemplo: R$ 300,00'}),
            'data_finalizar': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'style': 'max-width: 200px;',
                    'class': 'form-control'  # Opcional, para limitar a largura
                }
            ),
            'descricao': forms.Textarea(attrs={'class': 'form-control','style': 'width: 700px;', 'rows': 2, 'placeholder':'Faça a descrição do ticket'}),
        }

        data_finalizar = forms.DateField(
            widget=forms.DateInput(attrs={'type': 'date'}),
            input_formats=['%Y-%m-%d', '%d/%m/%Y']  # Formatos aceitos
        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Verifica se o usuário é superusuário
            if not self.instance.pk:  # Só se o objeto for novo
                if not self.user.is_superuser:
                    self.fields['emergencial'].widget = forms.HiddenInput()
                    self.fields['emergencial'].required = False
        
