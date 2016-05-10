# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0051_jacets_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='skateboards',
            name='price',
            field=models.IntegerField(verbose_name='Цена', null=True, blank=True),
        ),
    ]
