# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gushi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audioinfo_user',
            old_name='title',
            new_name='audioInfo',
        ),
        migrations.RenameField(
            model_name='audioinfo_user',
            old_name='name',
            new_name='user',
        ),
    ]
