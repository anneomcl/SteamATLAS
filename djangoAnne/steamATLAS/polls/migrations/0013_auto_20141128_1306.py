# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_owns_achievementspercentage'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='owns',
            unique_together=set([('appID', 'steamID')]),
        ),
    ]
