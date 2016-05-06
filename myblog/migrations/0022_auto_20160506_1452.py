# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0021_skateboards_type_skate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backpacks',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Наименование', blank=True, null=True, max_length=255)),
                ('size', models.SlugField(choices=[('S', 'Маленький'), ('M', 'Средний'), ('L', 'Большой')], null=True, verbose_name='Размер', blank=True)),
                ('image', models.ImageField(verbose_name='Фото', upload_to='', width_field='width_field', height_field='height_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(to='myblog.Brands')),
            ],
            options={
                'verbose_name': 'Рюкзак',
                'verbose_name_plural': 'Рюкзаки',
                'db_table': 'Рюкзаки',
            },
        ),
        migrations.AlterField(
            model_name='skateboards',
            name='type_skate',
            field=models.SlugField(choices=[('skateboard', 'Обычный скейтборд'), ('longboard', 'Лонгборд')], null=True, verbose_name='Тип скейтборда', blank=True),
        ),
    ]
