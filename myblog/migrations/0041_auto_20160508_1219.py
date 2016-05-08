# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0040_auto_20160508_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoes',
            name='size_41',
        ),
        migrations.RemoveField(
            model_name='shoes',
            name='size_42',
        ),
        migrations.RemoveField(
            model_name='shoes',
            name='size_43',
        ),
        migrations.AddField(
            model_name='shoes',
            name='size',
            field=models.BigIntegerField(verbose_name='Размер', blank=True, null=True),
        ),
    ]
