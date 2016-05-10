# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0053_remove_spectacles_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='spectacles',
            name='price',
            field=models.IntegerField(verbose_name='Цена', blank=True, null=True),
        ),
    ]
