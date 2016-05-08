# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0044_shoes_size_41'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('material', models.CharField(max_length=255, verbose_name='Материал')),
                ('created', models.DateTimeField(verbose_name='Дата', auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Материалы',
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
            },
        ),
        migrations.AlterField(
            model_name='shoes',
            name='material',
            field=models.ForeignKey(to='myblog.Materials', blank=True, null=True),
        ),
    ]
