# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('audioId', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('audioTitle', models.CharField(max_length=100)),
                ('audioType', models.CharField(max_length=20)),
                ('audioDate', models.CharField(max_length=20, blank=True)),
                ('audioUrl', models.CharField(max_length=80)),
                ('audioImageUrl', models.CharField(max_length=80)),
                ('audioLrcUrl', models.CharField(max_length=80)),
                ('audioText', models.TextField()),
                ('audioPartEndTime', models.CharField(max_length=50)),
                ('audioTextBlankIndex', models.TextField(blank=True)),
                ('audioStandardAnswer', models.TextField(blank=True)),
                ('avgCorrectRate', models.FloatField(max_length=10, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('userWrongWords', models.TextField(blank=True)),
                ('userCorrectRate', models.FloatField(max_length=8, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAudioBehavior',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isCollected', models.BooleanField(default=False)),
                ('userAnswer', models.TextField(blank=True)),
                ('audioCorrectRate', models.FloatField(max_length=8, blank=True)),
                ('audioId', models.ForeignKey(to='DataManager.Audio')),
                ('userId', models.ForeignKey(to='DataManager.User')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('wordId', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('word', models.CharField(max_length=50)),
                ('audioIdList', models.TextField()),
            ],
        ),
    ]
