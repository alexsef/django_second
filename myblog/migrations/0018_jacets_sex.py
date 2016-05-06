# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0017_auto_20160506_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='jacets',
            name='sex',
            field=models.SlugField(null=True, verbose_name='Пол', blank=True, choices=[('man', 'Мужская'), ('woman', 'Женская')]),
        ),
    ]
