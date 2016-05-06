# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0020_skateboards'),
    ]

    operations = [
        migrations.AddField(
            model_name='skateboards',
            name='type_skate',
            field=models.SlugField(blank=True, choices=[('skateboard', 'Обычный скейтборд'), ('longboard', 'ЛонгБорд')], verbose_name='Тип скейтборда', null=True),
        ),
    ]
