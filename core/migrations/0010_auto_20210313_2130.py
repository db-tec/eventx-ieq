# Generated by Django 3.1.7 on 2021-03-14 00:30

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210313_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to='eventos', verbose_name='Imagem'),
        ),
    ]
