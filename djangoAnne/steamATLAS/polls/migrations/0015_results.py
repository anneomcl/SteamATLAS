# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20141201_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='results',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('app_ID', models.IntegerField(null='true', default=0)),
                ('price', models.IntegerField(null='true', default=0)),
                ('score', models.IntegerField(null='true', default=0)),
                ('description', models.TextField(null='true', max_length=1000, default='None')),
                ('name', models.CharField(null='true', max_length=100, default='None')),
                ('tags', models.TextField(null='true', max_length=1000, default='None')),
                ('image', models.ImageField(upload_to='', null='true', max_length=1000, default='batman')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
