from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Orcamento
from ticket.models import Ticket
from .forms import OrcamenttoForm

def orcamento(request, id_ticket):
    form = OrcamenttoForm()
    ticket = Ticket.objects.get(pk=id_ticket)

    if request.method == 'POST':        
        form = OrcamenttoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.ticket = ticket  # Alterado para armazenar o objeto, não apenas o ID
            obj.save()
            messages.add_message(request, messages.SUCCESS, "Orçamento criado com sucesso!")
            return redirect('index-orcamento', id_ticket)
    else:

        orcamento = Orcamento.objects.filter(ticket=id_ticket).first()
        #return HttpResponse(orcamento)
        
        context = {
            'form': form,
            'orcamento': orcamento,
            'id_ticket': id_ticket
        }
    
    return render(request, 'orcamento/index-orcamento.html', context)

def lista_orcamento(request, id_orcamento):
    orcamento = Orcamento.objects.get(id=id_orcamento)
    context = {
        'orcamento':orcamento,
    }
    return render(request, 'orcamento/lista-orcamento.html', context)