from django.db import models

from django.contrib.auth.models import User

class Colaborador(models.Model):
    nomeCol = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    telefone = models.CharField(max_length=11)
    cpf_cnpj = models.CharField(max_length=20, null=True, unique=True)
    pix = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    enderecoCol = models.TextField()

    def __str__(self):
        return self.nomeCol