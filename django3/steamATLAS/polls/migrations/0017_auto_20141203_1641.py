# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20141202_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='lastOnline',
            field=models.IntegerField(null='true', default=0),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='game',
            unique_together=set([('name', 'app_ID')]),
        ),
    ]
