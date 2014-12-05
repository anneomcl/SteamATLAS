# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20141025_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='score',
            field=models.IntegerField(null='true', default=0),
            preserve_default=True,
        ),
    ]
