# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0043_remove_shoes_size_41'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='size_41',
            field=models.BooleanField(default=1, verbose_name='Размер 41'),
            preserve_default=False,
        ),
    ]
