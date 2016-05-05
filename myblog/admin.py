from django.contrib import admin
from .models import Goods


class GoodsAdmin(admin.ModelAdmin):
    exclude = ('width_field', 'height_field')


admin.site.register(Goods, GoodsAdmin)