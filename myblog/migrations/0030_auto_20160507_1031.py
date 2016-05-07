# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0029_auto_20160507_1030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='backpacks',
            options={'verbose_name_plural': 'Рюкзаки', 'verbose_name': 'Рюкзак'},
        ),
        migrations.RemoveField(
            model_name='backpacks',
            name='sex',
        ),
        migrations.AddField(
            model_name='backpacks',
            name='size',
            field=models.SlugField(null=True, choices=[('S', 'Маленький'), ('M', 'Средний'), ('L', 'Большой')], verbose_name='Размер', blank=True),
        ),
        migrations.AlterModelTable(
            name='backpacks',
            table='Рюкзаки',
        ),
    ]
