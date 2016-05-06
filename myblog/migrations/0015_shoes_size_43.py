# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0014_shoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='size_43',
            field=models.BooleanField(verbose_name='Размер 43', default=1),
            preserve_default=False,
        ),
    ]
