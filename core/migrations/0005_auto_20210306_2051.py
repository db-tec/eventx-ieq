# Generated by Django 3.1.7 on 2021-03-06 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_evento_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
    ]