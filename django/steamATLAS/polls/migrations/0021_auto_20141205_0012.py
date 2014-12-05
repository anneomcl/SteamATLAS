# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20141204_1805'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GameResults',
            new_name='GameResults2',
        ),
        migrations.AddField(
            model_name='playerweights',
            name='theta',
            field=models.FloatField(null='true', default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.FloatField(null='true', default=0.0),
            preserve_default=True,
        ),
    ]
