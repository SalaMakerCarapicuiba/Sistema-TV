# Generated by Django 5.1.1 on 2024-09-20 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_notices_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notices',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]