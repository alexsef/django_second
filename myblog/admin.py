from django.contrib import admin
from .models import *


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created',)
    search_fields = ('title',)


class ShoesAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created', 'size_41', 'size_42', 'size_43')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created', 'brand')
    search_fields = ('title',)
    list_editable = ('size_41', 'size_42', 'size_43')


class JacetsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created', 'size_S', 'size_M', 'size_L', 'size_XL')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created',)
    search_fields = ('title',)
    list_editable = ('size_S', 'size_M', 'size_L', 'size_XL')


class BrandsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created',)
    search_fields = ('title',)


class SkateboardsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created',)
    search_fields = ('title',)


class BackpacksAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created',)
    search_fields = ('title',)


class SpectaclesAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created',)
    search_fields = ('__str__',)


class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created')
    exclude = ('width_field', 'height_field', 'created')
    list_filter = ('created',)
    search_fields = ('__str__',)


class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    list_filter = ('created',)
    exclude = ('created',)
    search_fields = ('__str__',)


class SnowboardsAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    list_filter = ('created',)
    exclude = ('width_field', 'height_field', 'created')
    search_fields = ('__str__',)


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Shoes, ShoesAdmin)
admin.site.register(Jacets, JacetsAdmin)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(Skateboards, SkateboardsAdmin)
admin.site.register(Backpacks, BackpacksAdmin)
admin.site.register(Spectacles, SpectaclesAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(Materials, MaterialsAdmin)
admin.site.register(Snowboards, SnowboardsAdmin)
