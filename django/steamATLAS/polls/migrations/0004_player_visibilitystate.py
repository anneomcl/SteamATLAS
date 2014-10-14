# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_player_visibilitystate'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='visibilityState',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
