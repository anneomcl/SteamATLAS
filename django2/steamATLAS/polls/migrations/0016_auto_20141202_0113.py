# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_results'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='results',
            new_name='GameResults',
        ),
    ]
