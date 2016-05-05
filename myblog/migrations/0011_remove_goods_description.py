# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_auto_20160505_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='description',
        ),
    ]
