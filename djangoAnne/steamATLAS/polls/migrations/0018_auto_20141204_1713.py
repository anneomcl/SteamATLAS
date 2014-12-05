# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20141204_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='profirleURL',
            new_name='profileURL',
        ),
    ]
