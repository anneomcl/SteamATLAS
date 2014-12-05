# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20141204_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerWeights',
            fields=[
                ('steamID', models.IntegerField(serialize=False, default=1, primary_key=True)),
                ('weight', models.TextField(default='none', max_length=10000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='player',
            name='profileURL',
        ),
        migrations.AddField(
            model_name='player',
            name='profirleURL',
            field=models.TextField(default='none', max_length=1000),
            preserve_default=True,
        ),
    ]
