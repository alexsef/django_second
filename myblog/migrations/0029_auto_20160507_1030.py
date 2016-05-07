# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0028_auto_20160507_1020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='backpacks',
            options={'verbose_name_plural': 'Очки', 'verbose_name': 'Очки'},
        ),
        migrations.RemoveField(
            model_name='backpacks',
            name='size',
        ),
        migrations.AddField(
            model_name='backpacks',
            name='sex',
            field=models.SlugField(choices=[('man', 'Man'), ('woman', 'Woman'), ('unisex', 'Unisex')], verbose_name='Пол', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jacets',
            name='sex',
            field=models.SlugField(choices=[('man', 'Man'), ('woman', 'Woman'), ('unisex', 'Unisex')], verbose_name='Пол', null=True, blank=True),
        ),
        migrations.AlterModelTable(
            name='backpacks',
            table='Очки',
        ),
    ]
