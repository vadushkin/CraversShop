from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import product_of_the_day, best_product, product


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
    list_display_links = (
        'id',
        'title',
    )
    list_filter = (
        'title',
        'slug',
    )
    search_fields = (
        'title',
        'slug',
    )
    prepopulated_fields = {
        'slug': ('title',),
    }
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
    readonly_fields = (
        'get_photo',
        'created_at',
        'updated_at',
    )

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
    list_display_links = (
        'id',
    )
    fields = (
        'quantity',
        'open',
        'product',
    )
    readonly_fields = (
        'created_at',
        'sold',
    )


class BestProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'created_at',
    )
    list_display_links = (
        'id',
    )
    fields = (
        'product',
    )
    readonly_fields = (
        'created_at',
    )


admin.site.register(product_of_the_day.ProductOfTheDay, ProductOfTheDayAdmin)
admin.site.register(best_product.BestProduct, BestProductAdmin)
admin.site.register(product.Product, ProductAdmin)
