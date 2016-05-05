# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0012_goods_image_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='image_1',
        ),
    ]
