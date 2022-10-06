from django.contrib import admin
from django.utils.safestring import mark_safe
from django_mptt_admin.admin import DjangoMpttAdmin

from shop.models import social_network, category, product, product_of_the_day, best_product


class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'url',
        'photo',
        'get_photo')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name', 'url')
    fields = (
        'name',
        'photo',
        'url',
    )
    readonly_fields = ('get_photo',)

    @staticmethod
    def get_photo(obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return 'Фотографии нет'


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
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'parent', 'is_menu_field', 'photo',)
    readonly_fields = ('get_photo',)

    @staticmethod
    def get_photo(obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return 'Фотографии нет'


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'description',
        'category',
        'price',
        'sale',
        'is_on_closeout',
        'stars',
        'get_photo',
    )
    list_display_links = ('id', 'title',)
    list_filter = ('title', 'slug',)
    search_fields = ('title', 'slug',)
    prepopulated_fields = {"slug": ("title",)}
    fields = (
        'title',
        'slug',
        'description',
        'price',
        'category',
        'photo',
        'photo_back',
        'updated_at',
        'created_at',
        'sale',
        'stars',
        'is_on_closeout',
    )
    readonly_fields = ('get_photo', 'created_at', 'updated_at')

    @staticmethod
    def get_photo(obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return 'Фотографии нет'


class ProductOfTheDayAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'quantity',
        'open',
        'sold',
        'product',
        'created_at',
    )
    list_display_links = ('id',)
    fields = (
        'quantity',
        'open',
        'product',
    )
    readonly_fields = ('created_at', 'sold',)


class BestProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'created_at',
    )
    list_display_links = ('id',)
    fields = (
        'product',
    )
    readonly_fields = ('created_at',)


admin.site.register(social_network.Network, SocialNetworkAdmin)
admin.site.register(category.Category, CategoryAdmin)
admin.site.register(product.Product, ProductAdmin)
admin.site.register(product_of_the_day.ProductOfTheDay, ProductOfTheDayAdmin)
admin.site.register(best_product.BestProduct, BestProductAdmin)
