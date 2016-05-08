# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0046_auto_20160508_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='backpacks',
            name='material',
            field=models.ForeignKey(null=True, to='myblog.Materials', verbose_name='Материал', blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='material',
            field=models.ForeignKey(null=True, to='myblog.Materials', verbose_name='Материал', blank=True),
        ),
        migrations.AlterField(
            model_name='jacets',
            name='material',
            field=models.ForeignKey(null=True, to='myblog.Materials', verbose_name='Материал', blank=True),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='material',
            field=models.ForeignKey(null=True, to='myblog.Materials', verbose_name='Материал', blank=True),
        ),
    ]
