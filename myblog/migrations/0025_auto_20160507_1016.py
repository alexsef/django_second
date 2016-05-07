# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0024_auto_20160507_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backpacks',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jacets',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='skateboards',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
