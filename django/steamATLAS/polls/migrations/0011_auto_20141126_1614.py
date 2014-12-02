# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_game_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.TextField(null='true', default='batman', max_length=1000),
            preserve_default=True,
        ),
    ]
