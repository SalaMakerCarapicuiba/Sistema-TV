# Generated by Django 5.1.1 on 2024-10-07 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_materia'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='horario_de_inicio',
            field=models.TimeField(null=True),
        ),
    ]