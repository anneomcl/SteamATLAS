# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.CharField(default='None', max_length=1000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(default='None', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='app_ID',
            field=models.IntegerField(default=0),
        ),
    ]
