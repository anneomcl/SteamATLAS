# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20141126_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='owns',
            name='achievementsPercentage',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
