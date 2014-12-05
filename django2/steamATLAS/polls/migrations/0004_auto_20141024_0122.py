# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20141024_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='achieved',
            name='app_ID',
            field=models.IntegerField(default=0, null='true'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='achieved',
            name='name',
            field=models.TextField(max_length=1000, null='true', default='none'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='achieved',
            name='steamID',
            field=models.IntegerField(default=1, null='true'),
            preserve_default=True,
        ),
    ]
