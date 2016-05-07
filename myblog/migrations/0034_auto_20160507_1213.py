# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0033_auto_20160507_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='created',
            field=models.DateTimeField(verbose_name='Дата поступления', null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='backpacks',
            name='created',
            field=models.DateTimeField(verbose_name='Дата поступления', null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='brands',
            name='created',
            field=models.DateTimeField(verbose_name='Дата основания', null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='created',
            field=models.DateTimeField(verbose_name='Дата поступления', null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='jacets',
            name='created',
            field=models.DateTimeField(verbose_name='Дата поступления', null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='skateboards',
            name='created',
            field=models.DateTimeField(verbose_name='Дата поступления', null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='snowboards',
            name='created',
            field=models.DateTimeField(verbose_name='Дата поступления', null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='spectacles',
            name='created',
            field=models.DateTimeField(verbose_name='Дата поступления', null=True, auto_now_add=True),
        ),
    ]
