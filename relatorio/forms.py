from django import forms

class FiltroForm(forms.Form):
    CHOICES = [
        ('L', 'Levantamento'),
        ('O', 'Orçamento'),
        ('A', 'Aprovado'),
        ('V', 'Vistoriado'),
        ('F', 'Finalizado'),
    ]

    selected_option = forms.ChoiceField(
        choices=CHOICES, 
        widget=forms.RadioSelect(attrs={'class': 'form-control', 'style': 'width: 200px;'}),
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
