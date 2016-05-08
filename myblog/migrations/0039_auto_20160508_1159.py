# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0038_shoes_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='price',
            field=models.BigIntegerField(max_length=9, blank=True, null=True, verbose_name='Цена'),
        ),
    ]
