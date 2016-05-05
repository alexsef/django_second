# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20160505_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='img_1',
        ),
        migrations.AddField(
            model_name='goods',
            name='image',
            field=models.ImageField(height_field='height_field', default=1, upload_to='', verbose_name='Обложка', width_field='width_field'),
            preserve_default=False,
        ),
    ]
