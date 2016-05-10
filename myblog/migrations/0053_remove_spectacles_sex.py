# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0052_skateboards_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spectacles',
            name='sex',
        ),
    ]
