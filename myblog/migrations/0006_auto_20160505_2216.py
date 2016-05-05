# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_goods_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name_plural': 'Кепки', 'verbose_name': 'Кепка'},
        ),
        migrations.RemoveField(
            model_name='goods',
            name='category',
        ),
    ]
