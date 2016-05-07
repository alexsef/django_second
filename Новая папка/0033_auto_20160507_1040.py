# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0032_auto_20160507_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glasses',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(blank=True, null=True, max_length=255, verbose_name='Наименование')),
                ('image', models.ImageField(height_field='height_field', upload_to='', verbose_name='Фото', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('sex', models.SlugField(blank=True, choices=[('man', 'Man'), ('woman', 'Woman'), ('unisex', 'Unisex')], verbose_name='Пол', null=True)),
                ('brand', models.ForeignKey(to='myblog.Brands')),
            ],
            options={
                'verbose_name_plural': 'Очки',
                'db_table': 'Очки',
                'verbose_name': 'Очки',
            },
        ),
        migrations.RemoveField(
            model_name='spectacles',
            name='brand',
        ),
        migrations.DeleteModel(
            name='Spectacles',
        ),
    ]
