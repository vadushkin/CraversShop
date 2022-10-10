from django.contrib import admin
from django.utils.safestring import mark_safe
from django_mptt_admin.admin import DjangoMpttAdmin

from shop.models import category, popular_categories, brand_directory


class CategoryAdmin(DjangoMpttAdmin):
    list_display = (
        'title',
        'parent',
        'is_menu_field',
        'get_photo',
        'slug',
        'id',
    )
    list_display_links = ('id', 'title',)
    list_filter = ('title', 'slug',)
    search_fields = ('title', 'slug',)
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'parent', 'is_menu_field', 'photo',)
    readonly_fields = ('get_photo',)

    @staticmethod
    def get_photo(obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return 'Фотографии нет'


class PopularCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
    )
    list_display_links = ('id',)
    list_filter = ('category',)
    search_fields = (
        'category',
    )
    fields = (
        'category',
    )


class BrandDirectoryCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    list_display_links = ('id', 'name',)
    search_fields = (
        'name',
    )
    fields = (
        'name',
        'product',
    )


admin.site.register(category.Category, CategoryAdmin)
admin.site.register(popular_categories.PopularCategory, PopularCategoryAdmin)
admin.site.register(brand_directory.BrandDirectoryCategory, BrandDirectoryCategoryAdmin)
