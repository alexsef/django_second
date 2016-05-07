# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0026_auto_20160507_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
