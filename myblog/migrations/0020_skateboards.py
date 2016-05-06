# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0019_auto_20160506_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skateboards',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(null=True, verbose_name='Наименование', blank=True, max_length=255)),
                ('size', models.SlugField(null=True, verbose_name='Размер', choices=[('7.5', '7.5'), ('8', '8'), ('8.25', '8.25')], blank=True)),
                ('image', models.ImageField(verbose_name='Фото', upload_to='', height_field='height_field', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(to='myblog.Brands')),
            ],
            options={
                'verbose_name': 'Скейтборд',
                'db_table': 'Скейтборды',
                'verbose_name_plural': 'Скейтборды',
            },
        ),
    ]
