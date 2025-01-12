from django.db import models

from django.contrib.auth.models import User


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    gerente_loja = models.CharField(max_length=100)
    telefone = models.CharField(max_length=13)
    gerente_regional = models.CharField(max_length=100)
    enderecoCli = models.TextField()

    def __str__(self):
        return self.nome