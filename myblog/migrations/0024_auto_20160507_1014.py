# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0023_auto_20160507_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
