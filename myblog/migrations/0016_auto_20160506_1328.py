# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0015_shoes_size_43'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('brand', models.CharField(blank=True, null=True, verbose_name='Брэнд', max_length=255)),
                ('description', models.TextField(null=True, blank=True, verbose_name='Описание')),
            ],
            options={
                'db_table': 'Брэнды',
                'verbose_name': 'Брэнд',
                'verbose_name_plural': 'Брэнды',
            },
        ),
        migrations.CreateModel(
            name='MansJacets',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(blank=True, null=True, verbose_name='Наименование', max_length=255)),
                ('image', models.ImageField(upload_to='', height_field='height_field', verbose_name='Фото', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('material', models.CharField(blank=True, null=True, verbose_name='Материал', max_length=255)),
                ('style', models.CharField(blank=True, null=True, verbose_name='Фасон', max_length=255)),
                ('color', models.CharField(blank=True, null=True, verbose_name='Цвет', max_length=255)),
                ('size_S', models.BooleanField(verbose_name='Размер S')),
                ('size_M', models.BooleanField(verbose_name='Размер M')),
                ('size_L', models.BooleanField(verbose_name='Размер L')),
                ('size_XL', models.BooleanField(verbose_name='Размер XL')),
                ('brand', models.ForeignKey(to='myblog.Brands')),
            ],
            options={
                'db_table': 'Мужские куртки',
                'verbose_name': 'Мужская куртка',
                'verbose_name_plural': 'Мужские куртки',
            },
        ),
        migrations.AlterField(
            model_name='goods',
            name='brand',
            field=models.ForeignKey(default=1, to='myblog.Brands'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shoes',
            name='brand',
            field=models.ForeignKey(default=1, to='myblog.Brands'),
            preserve_default=False,
        ),
    ]
