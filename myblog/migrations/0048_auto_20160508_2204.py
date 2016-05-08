# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0047_auto_20160508_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jacets',
            name='sex',
            field=models.CharField(null=True, choices=[('man', 'Man'), ('woman', 'Woman'), ('unisex', 'Unisex')], blank=True, max_length=255, verbose_name='Пол'),
        ),
    ]
