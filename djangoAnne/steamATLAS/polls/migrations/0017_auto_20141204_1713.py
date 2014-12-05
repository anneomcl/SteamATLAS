# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20141202_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='profileURL',
        ),
        migrations.AddField(
            model_name='player',
            name='profirleURL',
            field=models.TextField(max_length=1000, default='none'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='activityState',
            field=models.IntegerField(default=1, null='true'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='avatar',
            field=models.TextField(max_length=1000, default='none', null='true'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='lastOnline',
            field=models.IntegerField(default=0, null='true'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='visibilityState',
            field=models.IntegerField(default=1, null='true'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='game',
            unique_together=set([('name', 'app_ID')]),
        ),
    ]
