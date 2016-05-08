# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0037_auto_20160508_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='price',
            field=models.BigIntegerField(max_length=255, blank=True, null=True, verbose_name='Цена'),
        ),
    ]
