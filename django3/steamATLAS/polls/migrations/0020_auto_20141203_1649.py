# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_auto_20141203_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='visibilityState',
            field=models.IntegerField(null='true', default=1),
            preserve_default=True,
        ),
    ]
