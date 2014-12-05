# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='tags',
            field=models.TextField(default='None', max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(default='None', max_length=1000),
        ),
    ]
