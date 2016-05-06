# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0013_remove_goods_image_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('brand', models.SlugField(max_length=255, blank=True, choices=[('vans', 'vans'), ('element', 'element'), ('dc', 'dc'), ('truespin', 'truespin')], verbose_name='Брэнд', null=True)),
                ('title', models.CharField(max_length=255, verbose_name='Наименование', blank=True, null=True)),
                ('image', models.ImageField(height_field='height_field', verbose_name='Фото', upload_to='', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=255, verbose_name='Цвет', blank=True, null=True)),
                ('size_41', models.BooleanField(verbose_name='Размер 41')),
                ('size_42', models.BooleanField(verbose_name='Размер 42')),
            ],
            options={
                'verbose_name': 'Обувь',
                'verbose_name_plural': 'Обувь',
                'db_table': 'Обувь',
            },
        ),
    ]
