# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0054_spectacles_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessories',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
    ]
