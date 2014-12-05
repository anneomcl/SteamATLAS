# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_gameresults2_steamid'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameresults2',
            name='tag_list',
            field=models.TextField(max_length=1000, null='true', default='None'),
            preserve_default=True,
        ),
    ]
