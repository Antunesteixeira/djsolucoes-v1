# Generated by Django 4.2.17 on 2025-04-07 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('O', 'Orçamento'), ('A', 'Aprovado'), ('E', 'Executado'), ('V', 'Vistoriado'), ('F', 'Finalizado'), ('R', 'Rejeitado')], default='L', max_length=1),
        ),
    ]
