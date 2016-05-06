from django.contrib import admin
from .models import Goods, Shoes, Jacets, Brands, Skateboards, Backpacks


class GoodsAdmin(admin.ModelAdmin):
    exclude = ('width_field', 'height_field')


class ShoesAdmin(admin.ModelAdmin):
    exclude = ('width_field', 'height_field')


class JacetsAdmin(admin.ModelAdmin):
    exclude = ('width_field', 'height_field')


class BrandsAdmin(admin.ModelAdmin):
    exclude = ('width_field', 'height_field')


class SkateboardsAdmin(admin.ModelAdmin):
    exclude = ('width_field', 'height_field')


class BackpacksAdmin(admin.ModelAdmin):
    exclude = ('width_field', 'height_field')


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Shoes, ShoesAdmin)
admin.site.register(Jacets, JacetsAdmin)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(Skateboards, SkateboardsAdmin)
admin.site.register(Backpacks, BackpacksAdmin)
