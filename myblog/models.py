from django.db import models
from datetime import datetime


brand_ch = (
    ('vans', 'vans'),
    ('element', 'element'),
    ('dc', 'dc'),
    ('truespin', 'truespin'),
)


class Goods(models.Model):
    class Meta:
        db_table = 'Товары'
        verbose_name = 'Кепка'
        verbose_name_plural = 'Кепки'

    brand = models.SlugField(max_length=255, verbose_name='Брэнд', choices=brand_ch, blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name='Наименование', blank=True, null=True)
    image = models.ImageField(width_field='width_field',
                              height_field='height_field',
                              verbose_name='Фото')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    material = models.CharField(max_length=255, verbose_name='Материал', blank=True, null=True)
    style = models.CharField(max_length=255, verbose_name='Фасон', blank=True, null=True)
    color = models.CharField(max_length=255, verbose_name='Цвет', blank=True, null=True)

    def __str__(self):
        return '%s' % (self.title)

