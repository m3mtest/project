# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disk', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='headImag',
            new_name='headImg',
        ),
    ]
