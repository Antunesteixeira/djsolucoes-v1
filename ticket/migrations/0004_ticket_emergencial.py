# Generated by Django 5.1.4 on 2025-01-14 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_alter_ticket_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='emergencial',
            field=models.BooleanField(default=False),
        ),
    ]
