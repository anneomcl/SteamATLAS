# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20141012_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='app_ID',
            field=models.IntegerField(null='true', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(max_length=1000, null='true', default='None'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=100, null='true', default='None'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.IntegerField(null='true', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='tags',
            field=models.TextField(max_length=1000, null='true', default='None'),
            preserve_default=True,
        ),
    ]
