# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0008_auto_20160505_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='briefly_description',
        ),
    ]
