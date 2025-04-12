from django import forms

from .models import Orcamento

class OrcamenttoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['item', 'etapa']