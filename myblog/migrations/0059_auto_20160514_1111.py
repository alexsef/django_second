# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0058_auto_20160514_1110'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoes',
            options={'ordering': ['-title'], 'verbose_name': 'Обувь', 'verbose_name_plural': 'Обувь'},
        ),
    ]
