# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20141205_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameresults2',
            name='steamID',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
