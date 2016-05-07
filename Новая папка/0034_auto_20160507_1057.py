# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0033_auto_20160507_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glasses',
            name='brand',
        ),
        migrations.DeleteModel(
            name='Glasses',
        ),
    ]
