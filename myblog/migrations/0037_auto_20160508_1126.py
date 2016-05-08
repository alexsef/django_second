# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0036_auto_20160507_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Belts',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Наименование', null=True, max_length=255, blank=True)),
                ('image', models.ImageField(verbose_name='Фото', height_field='height_field', upload_to='', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления', null=True)),
                ('sex', models.SlugField(verbose_name='Пол', choices=[('man', 'Man'), ('woman', 'Woman'), ('unisex', 'Unisex')], null=True, blank=True)),
                ('brand', models.ForeignKey(to='myblog.Brands')),
            ],
            options={
                'verbose_name_plural': 'Ремни',
                'verbose_name': 'Ремень',
                'db_table': 'Ремни',
            },
        ),
        migrations.AddField(
            model_name='shoes',
            name='material',
            field=models.CharField(verbose_name='Материал', null=True, max_length=255, blank=True),
        ),
    ]
