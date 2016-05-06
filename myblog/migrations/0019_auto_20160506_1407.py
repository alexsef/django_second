# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0018_jacets_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jacets',
            name='sex',
            field=models.SlugField(verbose_name='Пол', choices=[('man', 'Мужская куртка'), ('woman', 'Женская куртка')], null=True, blank=True),
        ),
    ]
