# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0049_auto_20160508_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='price',
            field=models.IntegerField(blank=True, verbose_name='Цена', null=True),
        ),
    ]
