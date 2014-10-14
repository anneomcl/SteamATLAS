# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20141012_0414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='visibilityState',
        ),
    ]
