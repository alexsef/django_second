# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0045_auto_20160508_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='material',
            field=models.ForeignKey(null=True, blank=True, to='myblog.Materials'),
        ),
        migrations.AlterField(
            model_name='jacets',
            name='material',
            field=models.ForeignKey(null=True, blank=True, to='myblog.Materials'),
        ),
    ]
