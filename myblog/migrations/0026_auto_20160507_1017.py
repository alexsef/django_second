# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0025_auto_20160507_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
