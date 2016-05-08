# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0048_auto_20160508_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='sex',
            field=models.CharField(blank=True, choices=[('man', 'Man'), ('woman', 'Woman'), ('unisex', 'Unisex')], max_length=255, verbose_name='Пол', null=True),
        ),
        migrations.AlterField(
            model_name='backpacks',
            name='size',
            field=models.CharField(blank=True, choices=[('S', 'Маленький'), ('M', 'Средний'), ('L', 'Большой')], max_length=255, verbose_name='Размер', null=True),
        ),
        migrations.AlterField(
            model_name='belts',
            name='sex',
            field=models.CharField(blank=True, choices=[('man', 'Man'), ('woman', 'Woman'), ('unisex', 'Unisex')], max_length=255, verbose_name='Пол', null=True),
        ),
        migrations.AlterField(
            model_name='skateboards',
            name='size',
            field=models.CharField(blank=True, choices=[('7.5', '7.5'), ('8', '8'), ('8.25', '8.25')], max_length=255, verbose_name='Размер', null=True),
        ),
        migrations.AlterField(
            model_name='skateboards',
            name='type_skate',
            field=models.CharField(blank=True, choices=[('skateboard', 'Обычный скейтборд'), ('longboard', 'Лонгборд')], max_length=255, verbose_name='Тип скейтборда', null=True),
        ),
        migrations.AlterField(
            model_name='snowboards',
            name='sex',
            field=models.CharField(blank=True, choices=[('man', 'Man'), ('woman', 'Woman'), ('unisex', 'Unisex')], max_length=255, verbose_name='Пол', null=True),
        ),
        migrations.AlterField(
            model_name='snowboards',
            name='size',
            field=models.CharField(blank=True, choices=[('150', '150'), ('160', '160'), ('170', '170')], max_length=255, verbose_name='Размер', null=True),
        ),
        migrations.AlterField(
            model_name='spectacles',
            name='sex',
            field=models.CharField(blank=True, choices=[('man', 'Man'), ('woman', 'Woman'), ('unisex', 'Unisex')], max_length=255, verbose_name='Пол', null=True),
        ),
    ]
