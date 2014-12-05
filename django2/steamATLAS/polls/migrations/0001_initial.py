# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achieved',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('steamID', models.IntegerField(default=1)),
                ('name', models.TextField(default='none', max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.TextField(default='none', max_length=1000)),
                ('appID', models.IntegerField(default=1)),
                ('description', models.TextField(default='none', max_length=1000)),
                ('globalAP', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('app_ID', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(default='None', max_length=1000)),
                ('name', models.CharField(default='None', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Owns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('totalPlaytime', models.IntegerField(default=1)),
                ('recentlyPlaced', models.IntegerField(default=1)),
                ('appID', models.IntegerField(default=1)),
                ('steamID', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('friends', models.TextField(default='none', max_length=1000)),
                ('lastOnline', models.IntegerField(default=0)),
                ('activityState', models.IntegerField(default=1)),
                ('steamID', models.IntegerField(primary_key=True, default=1, serialize=False)),
                ('displayName', models.TextField(default='none', max_length=1000)),
                ('profileURL', models.TextField(default='none', max_length=1000)),
                ('avatar', models.TextField(default='none', max_length=1000)),
                ('visibilityState', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='achievement',
            unique_together=set([('name', 'appID')]),
        ),
    ]
