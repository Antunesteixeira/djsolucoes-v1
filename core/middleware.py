from django.shortcuts import redirect
from django.contrib import messages

class SessionExpiryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verifica se o usuário está autenticado
        if request.user.is_authenticated:
            # Se a sessão não tiver uma chave, ela expirou
            if not request.session.session_key:
                messages.info(request, "Sua sessão expirou. Faça login novamente.")
                # Substitua 'login' pela URL da sua página de login
                return redirect('login')  

        response = self.get_response(request)
        return response
