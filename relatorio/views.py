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
            
            selected_option_user = form.cleaned_data['selected_option_user']
            
            create_date = form.cleaned_data['create_date']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            # Exemplo de uso do valor
            #print(f"Opção selecionada: {selected_option}")
            # Faça algo com o valor capturado, como salvar no banco de dados
            # Verificar se as datas foram informadas
            if create_date:
                if selected_option_user:
                    tickets = tickets.filter(status=selected_option, data_criacao=create_date, usuario=selected_option_user)
                else:
                    tickets = tickets.filter(status=selected_option, data_criacao=create_date)

            if start_date and end_date:
                # Filtrar entre as datas apenas se ambas forem fornecidas
                if selected_option_user:
                    tickets = tickets.filter(status=selected_option , ultimo_update__range=(start_date, end_date), usuario=selected_option_user)
                else:
                    tickets = tickets.filter(status=selected_option , ultimo_update__range=(start_date, end_date))
            elif start_date:
                # Filtrar a partir da data inicial
                if selected_option_user:
                    tickets = tickets.filter(status=selected_option, ultimo_update__gte=start_date, usuario=selected_option_user)
                else:
                    tickets = tickets.filter(status=selected_option, ultimo_update__gte=start_date)
            elif end_date:
                # Filtrar até a data final
                if selected_option_user:
                    tickets = tickets.filter(status=selected_option, ultimo_update__lte=end_date, usuario=selected_option_user)
                else:
                    tickets = tickets.filter(status=selected_option, ultimo_update__lte=end_date)
            else:
                if selected_option_user:
                    tickets = tickets.filter(status=selected_option, usuario=selected_option_user)
                else:
                    tickets = tickets.filter(status=selected_option)


            total_faturamento_bruto = sum(ticket.valor_faturamento for ticket in tickets)
            total_mao_obra = sum(ticket.valor_mao_obra for ticket in tickets)
            total_custo_material = sum(ticket.valor_custo for ticket in tickets)
            total_faturamento_liquido = total_faturamento_bruto - (total_mao_obra + total_custo_material)

            # Calcular a média da margem e arredondar para 4 casas decimais           
            if len(tickets) > 0:
                media_margem = round(sum(round(ticket.func_bdi(), 5) for ticket in tickets) / len(tickets), 4)
            else:
                media_margem = 0  # Caso não haja tickets, atribui 0 à média
        

            context = {
                'title': 'Relatórios',
                'form':form,
                'tickets': tickets,
                'total_faturamento_bruto':total_faturamento_bruto,
                'total_faturamento_liquido':total_faturamento_liquido,
                'total_mao_obra': total_mao_obra,
                'total_material': total_custo_material, 
                'media_margem': media_margem,
                'form': form,
            }

            return render(request, 'relatorio/relatorio-index.html', context)
        else:
            print("Formulário inválido")
    else:
        form = FiltroForm()

    return render(request, 'relatorio/relatorio-index.html', {'form': form})
