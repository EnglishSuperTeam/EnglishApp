# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('mp3_path', models.TextField()),
                ('pic_path', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AudioInfo_User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isGood', models.CharField(max_length=20)),
                ('Question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='audioinfo_user',
            name='name',
            field=models.ForeignKey(to='gushi.User'),
        ),
        migrations.AddField(
            model_name='audioinfo_user',
            name='title',
            field=models.ForeignKey(to='gushi.AudioInfo'),
        ),
    ]
