# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0035_auto_20160507_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='image',
            field=models.ImageField(upload_to='', width_field='width_field', blank=True, height_field='height_field', null=True, verbose_name='Фото'),
        ),
    ]
