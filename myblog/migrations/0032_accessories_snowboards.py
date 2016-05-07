# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0031_spectacles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Наименование', null=True, blank=True, max_length=255)),
                ('image', models.ImageField(upload_to='', height_field='height_field', verbose_name='Фото', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('sex', models.SlugField(choices=[('man', 'Man'), ('woman', 'Woman'), ('unisex', 'Unisex')], verbose_name='Пол', null=True, blank=True)),
                ('brand', models.ForeignKey(to='myblog.Brands')),
            ],
            options={
                'db_table': 'Аксессуары',
                'verbose_name': 'Аксессуар',
                'verbose_name_plural': 'Аксессуары',
            },
        ),
        migrations.CreateModel(
            name='Snowboards',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Наименование', null=True, blank=True, max_length=255)),
                ('image', models.ImageField(upload_to='', height_field='height_field', verbose_name='Фото', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('sex', models.SlugField(choices=[('man', 'Man'), ('woman', 'Woman'), ('unisex', 'Unisex')], verbose_name='Пол', null=True, blank=True)),
                ('size', models.SlugField(choices=[('150', '150'), ('160', '160'), ('170', '170')], verbose_name='Размер', null=True, blank=True)),
                ('brand', models.ForeignKey(to='myblog.Brands')),
            ],
            options={
                'db_table': 'Сноуборды',
                'verbose_name': 'Сноуборд',
                'verbose_name_plural': 'Сноуборды',
            },
        ),
    ]
