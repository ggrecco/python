# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('produto', models.CharField(max_length=50)),
                ('cveid', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=200)),
                ('dataCorrecao', models.CharField(max_length=50)),
                ('nota', models.CharField(max_length=10)),
                ('tipoAcesso', models.CharField(max_length=200)),
                ('comentario', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'entradas',
            },
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='entrada',
            name='servidor',
            field=models.ForeignKey(to='meu_projetos.Servidor'),
        ),
    ]
