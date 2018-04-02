# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cves', '0002_auto_20180402_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=200)),
                ('cveid', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=200)),
                ('datacorrecao', models.CharField(max_length=200)),
                ('nota', models.CharField(max_length=200)),
                ('acesso', models.CharField(max_length=200)),
                ('comentários', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
