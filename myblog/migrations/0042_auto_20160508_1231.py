# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0041_auto_20160508_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoes',
            name='size',
        ),
        migrations.AddField(
            model_name='shoes',
            name='size_41',
            field=models.BooleanField(verbose_name='Размер 41', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoes',
            name='size_42',
            field=models.BooleanField(verbose_name='Размер 42', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoes',
            name='size_43',
            field=models.BooleanField(verbose_name='Размер 43', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shoes',
            name='price',
            field=models.IntegerField(verbose_name='Цена', null=True, blank=True),
        ),
    ]
