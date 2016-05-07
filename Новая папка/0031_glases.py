# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0030_auto_20160507_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glases',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(blank=True, null=True, verbose_name='Наименование', max_length=255)),
                ('image', models.ImageField(upload_to='', verbose_name='Фото', height_field='height_field', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('sex', models.SlugField(blank=True, choices=[('man', 'Man'), ('woman', 'Woman'), ('unisex', 'Unisex')], null=True, verbose_name='Пол')),
                ('brand', models.ForeignKey(to='myblog.Brands')),
            ],
            options={
                'verbose_name': 'Очки',
                'db_table': 'Очки',
                'verbose_name_plural': 'Очки',
            },
        ),
    ]
