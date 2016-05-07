# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0034_auto_20160507_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='brands',
            name='image',
            field=models.ImageField(height_field='height_field', width_field='width_field', verbose_name='Фото', default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brands',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
