# Generated by Django 3.1.7 on 2021-03-06 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='foto_evento')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('data_inicial', models.DateTimeField(verbose_name='Entrada')),
                ('data_final', models.DateTimeField(verbose_name='Saída')),
                ('local', models.CharField(max_length=100, verbose_name='Endereço')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('telefone', models.CharField(max_length=18, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.evento')),
            ],
        ),
    ]
