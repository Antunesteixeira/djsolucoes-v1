from django.db import models

from ticket.models import Ticket

class Orcamento(models.Model):
    item = models.IntegerField()
    ticket= models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True)
    etapa = models.CharField(max_length=100)

    def __str__(self):
        return self.etapa
    
    

