# Generated by Django 5.1.1 on 2024-10-07 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_materia_horario_de_inicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='horario_de_termino',
            field=models.TimeField(null=True),
        ),
    ]
