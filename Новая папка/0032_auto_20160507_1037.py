# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0031_glases'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spectacles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(blank=True, verbose_name='Наименование', max_length=255, null=True)),
                ('image', models.ImageField(verbose_name='Фото', height_field='height_field', width_field='width_field', upload_to='')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('sex', models.SlugField(choices=[('man', 'Man'), ('woman', 'Woman'), ('unisex', 'Unisex')], blank=True, verbose_name='Пол', null=True)),
                ('brand', models.ForeignKey(to='myblog.Brands')),
            ],
            options={
                'db_table': 'Очочки',
                'verbose_name': 'Очочоки',
                'verbose_name_plural': 'Очочоки',
            },
        ),
        migrations.RemoveField(
            model_name='glases',
            name='brand',
        ),
        migrations.DeleteModel(
            name='Glases',
        ),
    ]
