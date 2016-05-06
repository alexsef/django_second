# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0016_auto_20160506_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jacets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(null=True, verbose_name='Наименование', blank=True, max_length=255)),
                ('image', models.ImageField(verbose_name='Фото', upload_to='', width_field='width_field', height_field='height_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('material', models.CharField(null=True, verbose_name='Материал', blank=True, max_length=255)),
                ('style', models.CharField(null=True, verbose_name='Фасон', blank=True, max_length=255)),
                ('color', models.CharField(null=True, verbose_name='Цвет', blank=True, max_length=255)),
                ('size_S', models.BooleanField(verbose_name='Размер S')),
                ('size_M', models.BooleanField(verbose_name='Размер M')),
                ('size_L', models.BooleanField(verbose_name='Размер L')),
                ('size_XL', models.BooleanField(verbose_name='Размер XL')),
                ('brand', models.ForeignKey(to='myblog.Brands')),
            ],
            options={
                'verbose_name': 'Куртка',
                'verbose_name_plural': 'Куртки',
                'db_table': 'Куртки',
            },
        ),
        migrations.RemoveField(
            model_name='mansjacets',
            name='brand',
        ),
        migrations.DeleteModel(
            name='MansJacets',
        ),
    ]
