# Generated by Django 5.1.1 on 2024-10-08 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_materia_horario_de_termino'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_de_inicio', models.TimeField(null=True)),
                ('horario_de_termino', models.TimeField(null=True)),
                ('periodo', models.IntegerField(choices=[(1, 'Matutino'), (2, 'Vespertino'), (3, 'Noturno')])),
            ],
        ),
        migrations.RemoveField(
            model_name='materia',
            name='horario_de_inicio',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='horario_de_termino',
        ),
    ]