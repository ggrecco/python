# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meu_projetos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('produto', models.CharField(max_length=50)),
                ('cveid', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=200)),
                ('dataCorrecao', models.CharField(max_length=50)),
                ('nota', models.CharField(max_length=10)),
                ('tipoAcesso', models.CharField(max_length=200)),
                ('comentario', models.TextField()),
                ('servidor', models.ForeignKey(to='meu_projetos.Servidor')),
            ],
            options={
                'verbose_name_plural': 'entradas',
            },
        ),
    ]
