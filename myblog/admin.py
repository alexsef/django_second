from django.contrib import admin
from .models import *


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created',)
    search_fields = ('title',)


class ShoesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created', 'brand')
    search_fields = ('title',)


class JacetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created',)
    search_fields = ('title',)


class BrandsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'created')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created',)
    search_fields = ('title',)


class SkateboardsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created',)
    search_fields = ('title',)


class BackpacksAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created',)
    search_fields = ('title',)


class SpectaclesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created',)
    search_fields = ('title',)


class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created',)
    search_fields = ('title',)


class BeltsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created',)
    search_fields = ('title',)


class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('material',)
    list_filter = ('created',)
    exclude = ('created',)
    search_fields = ('material',)


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Shoes, ShoesAdmin)
admin.site.register(Jacets, JacetsAdmin)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(Skateboards, SkateboardsAdmin)
admin.site.register(Backpacks, BackpacksAdmin)
admin.site.register(Spectacles, SpectaclesAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(Belts, BeltsAdmin)
admin.site.register(Materials, MaterialsAdmin)
