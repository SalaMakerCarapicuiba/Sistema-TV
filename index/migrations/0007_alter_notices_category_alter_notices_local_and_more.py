# Generated by Django 5.1.1 on 2024-09-27 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_alter_notices_content_alter_notices_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notices',
            name='category',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='notices',
            name='local',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='notices',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='notices',
            name='responsible',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='notices',
            name='subcategory',
            field=models.CharField(max_length=30),
        ),
    ]
