# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0057_auto_20160511_1246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoes',
            options={'verbose_name': 'Обувь', 'verbose_name_plural': 'Обувь', 'ordering': ['-created']},
        ),
    ]
