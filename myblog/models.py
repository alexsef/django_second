from django.db import models
# from datetime import datetime


class Brands(models.Model):
    class Meta:
        db_table = 'Брэнды'
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'

    brand = models.CharField(max_length=255, verbose_name='Брэнд', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return '%s' % (self.brand)


class Shoes(models.Model):
    class Meta:
        db_table = 'Обувь'
        verbose_name = 'Обувь'
        verbose_name_plural = 'Обувь'

    brand = models.ForeignKey(Brands)
    title = models.CharField(max_length=255, verbose_name='Наименование', blank=True, null=True)
    image = models.ImageField(width_field='width_field',
                              height_field='height_field',
                              verbose_name='Фото')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    color = models.CharField(max_length=255, verbose_name='Цвет', blank=True, null=True)
    size_41 = models.BooleanField(verbose_name='Размер 41')
    size_42 = models.BooleanField(verbose_name='Размер 42')
    size_43 = models.BooleanField(verbose_name='Размер 43')

    def __str__(self):
        return '%s' % (self.title)


class Goods(models.Model):
    class Meta:
        db_table = 'Товары'
        verbose_name = 'Кепка'
        verbose_name_plural = 'Кепки'

    brand = models.ForeignKey(Brands)
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


jacets_ch = (
    ('man', 'Мужская куртка'),
    ('woman', 'Женская куртка'),
)


class Jacets(models.Model):
    class Meta:
        db_table = 'Куртки'
        verbose_name = 'Куртка'
        verbose_name_plural = 'Куртки'

    sex = models.SlugField(verbose_name='Пол', choices=jacets_ch, blank=True, null=True)
    brand = models.ForeignKey(Brands)
    title = models.CharField(max_length=255, verbose_name='Наименование', blank=True, null=True)
    image = models.ImageField(width_field='width_field',
                              height_field='height_field',
                              verbose_name='Фото')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    material = models.CharField(max_length=255, verbose_name='Материал', blank=True, null=True)
    style = models.CharField(max_length=255, verbose_name='Фасон', blank=True, null=True)
    color = models.CharField(max_length=255, verbose_name='Цвет', blank=True, null=True)
    size_S = models.BooleanField(verbose_name='Размер S')
    size_M = models.BooleanField(verbose_name='Размер M')
    size_L = models.BooleanField(verbose_name='Размер L')
    size_XL = models.BooleanField(verbose_name='Размер XL')

    def __str__(self):
        return '%s' % (self.title)


skate_ch = (
    ('7.5', '7.5'),
    ('8', '8'),
    ('8.25', '8.25'),
)


type_sk = (
    ('skateboard', 'Обычный скейтборд'),
    ('longboard', 'Лонгборд'),
)



class Skateboards(models.Model):
    class Meta:
        db_table = 'Скейтборды'
        verbose_name = 'Скейтборд'
        verbose_name_plural = 'Скейтборды'

    brand = models.ForeignKey(Brands)
    type_skate = models.SlugField(verbose_name='Тип скейтборда', choices=type_sk, blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name='Наименование', blank=True, null=True)
    size = models.SlugField(verbose_name='Размер', choices=skate_ch, blank=True, null=True)
    image = models.ImageField(width_field='width_field',
                              height_field='height_field',
                              verbose_name='Фото')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.title)

backpacks_ch = (
    ('S', 'Маленький'),
    ('M', 'Средний'),
    ('L', 'Большой'),
)

class Backpacks(models.Model):
    class Meta:
        db_table = 'Рюкзаки'
        verbose_name = 'Рюкзак'
        verbose_name_plural = 'Рюкзаки'

    brand = models.ForeignKey(Brands)
    title = models.CharField(max_length=255, verbose_name='Наименование', blank=True, null=True)
    size = models.SlugField(verbose_name='Размер', choices=backpacks_ch, blank=True, null=True)
    image = models.ImageField(width_field='width_field',
                              height_field='height_field',
                              verbose_name='Фото')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.title)







