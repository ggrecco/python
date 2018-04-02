# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cves', '0003_auto_20180402_1953'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topic2',
            new_name='Topic',
        ),
    ]
