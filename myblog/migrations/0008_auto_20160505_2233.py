# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_auto_20160505_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='title',
            field=models.CharField(null=True, blank=True, verbose_name='Наименование', max_length=255),
        ),
    ]
