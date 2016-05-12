# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0056_snowboards_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='brand',
            field=models.ForeignKey(verbose_name='Брэнд', to='myblog.Brands'),
        ),
        migrations.AlterField(
            model_name='backpacks',
            name='brand',
            field=models.ForeignKey(verbose_name='Брэнд', to='myblog.Brands'),
        ),
        migrations.AlterField(
            model_name='belts',
            name='brand',
            field=models.ForeignKey(verbose_name='Брэнд', to='myblog.Brands'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='brand',
            field=models.ForeignKey(verbose_name='Брэнд', to='myblog.Brands'),
        ),
        migrations.AlterField(
            model_name='jacets',
            name='brand',
            field=models.ForeignKey(verbose_name='Брэнд', to='myblog.Brands'),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='brand',
            field=models.ForeignKey(verbose_name='Брэнд', to='myblog.Brands'),
        ),
        migrations.AlterField(
            model_name='skateboards',
            name='brand',
            field=models.ForeignKey(verbose_name='Брэнд', to='myblog.Brands'),
        ),
        migrations.AlterField(
            model_name='snowboards',
            name='brand',
            field=models.ForeignKey(verbose_name='Брэнд', to='myblog.Brands'),
        ),
        migrations.AlterField(
            model_name='spectacles',
            name='brand',
            field=models.ForeignKey(verbose_name='Брэнд', to='myblog.Brands'),
        ),
    ]
