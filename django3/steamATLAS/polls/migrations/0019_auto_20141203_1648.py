# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20141203_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='activityState',
            field=models.IntegerField(null='true', default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='avatar',
            field=models.TextField(null='true', max_length=1000, default='none'),
            preserve_default=True,
        ),
    ]
