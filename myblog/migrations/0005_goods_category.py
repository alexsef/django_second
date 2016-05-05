# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20160505_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.SlugField(default=1, verbose_name='Категория', max_length=255, choices=[('fiction', 'художественная'), ('technical', 'техническая'), ('science', 'научная'), ('detective', 'детектив')]),
            preserve_default=False,
        ),
    ]
