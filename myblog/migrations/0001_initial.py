# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('briefly_description', models.DateField(verbose_name='Краткое описание')),
                ('img_1', models.CharField(max_length=255, verbose_name='Изображение')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name_plural': 'Товары',
                'db_table': 'Товары',
                'verbose_name': 'Товар',
            },
        ),
    ]
