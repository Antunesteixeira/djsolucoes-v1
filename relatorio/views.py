from django.shortcuts import render, redirect
from ticket.models import Ticket
from .forms import FiltroForm

def relatorioViews(request):
    if request.method == 'POST':
        form = FiltroForm(request.POST or None)
        tickets = Ticket.objects.all()
        if form.is_valid():
            # Captura o valor do botão de rádio selecionado
            selected_option = form.cleaned_data['selected_option']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            # Exemplo de uso do valor
            #print(f"Opção selecionada: {selected_option}")
            # Faça algo com o valor capturado, como salvar no banco de dados
             # Verificar se as datas foram informadas
            if start_date and end_date:
                # Filtrar entre as datas apenas se ambas forem fornecidas
                tickets = tickets.filter(status=selected_option , ultimo_update__range=(start_date, end_date))
            elif start_date:
                # Filtrar a partir da data inicial
                tickets = tickets.filter(status=selected_option, ultimo_update__gte=start_date)
            elif end_date:
                # Filtrar até a data final
                tickets = tickets.filter(status=selected_option, ultimo_update__lte=end_date)
            else:
                tickets = tickets.filter(status=selected_option)
                
            context = {
                'title': 'Relatórios',
                'form':form,
                'tickets': tickets,
                'form': form,
            }

            return render(request, 'relatorio/relatorio-index.html', context)
        else:
            print("Formulário inválido")
    else:
        form = FiltroForm()

    return render(request, 'relatorio/relatorio-index.html', {'form': form})
