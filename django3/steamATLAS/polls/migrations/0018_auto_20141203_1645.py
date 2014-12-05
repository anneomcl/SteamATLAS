# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20141203_1641'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='game',
            unique_together=set([]),
        ),
    ]
