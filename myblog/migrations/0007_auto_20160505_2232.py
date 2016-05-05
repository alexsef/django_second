# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_auto_20160505_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='brand',
            field=models.SlugField(blank=True, null=True, verbose_name='Брэнд', choices=[('vans', 'vans'), ('element', 'element'), ('dc', 'dc'), ('truespin', 'truespin')], max_length=255),
        ),
        migrations.AddField(
            model_name='goods',
            name='color',
            field=models.CharField(null=True, verbose_name='Цвет', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='goods',
            name='material',
            field=models.CharField(null=True, verbose_name='Материал', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='goods',
            name='style',
            field=models.CharField(null=True, verbose_name='Фасон', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='goods',
            name='title',
            field=models.CharField(verbose_name='Наименование', max_length=255),
        ),
    ]
