# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0032_accessories_snowboards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='created',
            field=models.DateTimeField(null=True, verbose_name='Дата поступления', auto_now_add=True),
        ),
    ]
