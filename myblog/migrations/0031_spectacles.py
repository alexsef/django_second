# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0030_auto_20160507_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spectacles',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(null=True, max_length=255, blank=True, verbose_name='Наименование')),
                ('image', models.ImageField(width_field='width_field', height_field='height_field', upload_to='', verbose_name='Фото')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('sex', models.SlugField(null=True, blank=True, verbose_name='Пол', choices=[('man', 'Man'), ('woman', 'Woman'), ('unisex', 'Unisex')])),
                ('brand', models.ForeignKey(to='myblog.Brands')),
            ],
            options={
                'db_table': 'Очочки',
                'verbose_name_plural': 'Очки',
                'verbose_name': 'Очки',
            },
        ),
    ]
