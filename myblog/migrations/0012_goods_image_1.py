# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0011_remove_goods_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='image_1',
            field=models.ImageField(blank=True, height_field='height_field', width_field='width_field', verbose_name='Второе фото', upload_to='', null=True),
        ),
    ]
