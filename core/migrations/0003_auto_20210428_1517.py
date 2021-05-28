# Generated by Django 3.2 on 2021-04-28 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_pontoturistico_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='pontoturistico',
            name='status',
            field=models.BooleanField(verbose_name='Ativo'),
        ),
    ]