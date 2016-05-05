# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_remove_goods_briefly_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='goods',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
