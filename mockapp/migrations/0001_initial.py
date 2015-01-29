# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('postid', models.CharField(primary_key=True, serialize=False, max_length=40)),
                ('created_time', models.DateTimeField()),
                ('from_user', models.CharField(max_length=100)),
                ('retweeted_from', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.TextField()),
                ('retweets', models.IntegerField()),
                ('favorites', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
