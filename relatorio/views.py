from django.shortcuts import render, redirect
from ticket.models import Ticket
from .forms import FiltroForm

from django.contrib.auth.models import User, Group

from rolepermissions.roles import assign_role
from rolepermissions.checkers import has_role
from rolepermissions.decorators import has_role_decorator, has_permission_decorator

from django.contrib.auth.decorators import login_required

from decimal import Decimal

@login_required
def relatorioViews(request):
    if request.method == 'POST':
        if 'limpar' in request.POST:
            form = FiltroForm()
            return render(request, 'relatorio/relatorio-index.html', {'form': form})

        form = FiltroForm(request.POST or None)

        usuario = request.user
        if has_role(usuario, [User, 'super']):
            tickets = Ticket.objects.all()
        else:
            tickets = Ticket.objects.filter(usuario=request.user)
        
        if form.is_valid():
            # Captura o valor do botão de rádio selecionado
            selected_option = form.cleaned_data['selected_option']
            create_date = form.cleaned_data['create_date']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            # Exemplo de uso do valor
            #print(f"Opção selecionada: {selected_option}")
            # Faça algo com o valor capturado, como salvar no banco de dados
            # Verificar se as datas foram informadas
            if create_date:
                tickets = tickets.filter(status=selected_option, data_criacao=create_date)

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

            total_faturamento = sum(ticket.valor_faturamento for ticket in tickets) 

            
            context = {
                'title': 'Relatórios',
                'form':form,
                'tickets': tickets,
                'total_faturamento':total_faturamento, 
                'form': form,
            }

            return render(request, 'relatorio/relatorio-index.html', context)
        else:
            print("Formulário inválido")
    else:
        form = FiltroForm()

    return render(request, 'relatorio/relatorio-index.html', {'form': form})
