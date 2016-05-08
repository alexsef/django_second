# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0039_auto_20160508_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='price',
            field=models.BigIntegerField(null=True, verbose_name='Цена', blank=True),
        ),
    ]
