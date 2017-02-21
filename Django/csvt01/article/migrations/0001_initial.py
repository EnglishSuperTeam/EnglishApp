# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('image', models.TextField()),
                ('classification', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('is_crawled', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_url', models.URLField()),
                ('name', models.CharField(max_length=300)),
                ('crawled_date', models.CharField(max_length=30)),
                ('source_article', models.ManyToManyField(to='article.Article')),
                ('source_articleurl', models.ManyToManyField(to='article.ArticleUrl')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('tag_article', models.ManyToManyField(to='article.Article')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='User_Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_good', models.CharField(max_length=20)),
                ('is_bad', models.CharField(max_length=20)),
                ('is_skipped', models.CharField(max_length=20)),
                ('read_date', models.DateField(auto_now_add=True)),
                ('article', models.ForeignKey(to='article.Article')),
                ('user', models.ForeignKey(to='article.User')),
            ],
        ),
        migrations.CreateModel(
            name='User_Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_weight', models.FloatField(max_length=20)),
                ('article', models.ForeignKey(to='article.Article')),
                ('user', models.ForeignKey(to='article.User')),
            ],
        ),
        migrations.AddField(
            model_name='articleurl',
            name='articleUrl_source',
            field=models.OneToOneField(to='article.Source'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_source',
            field=models.ManyToManyField(to='article.Source'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_tag',
            field=models.ManyToManyField(to='article.Tag'),
        ),
    ]
