from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import banner, lower_banner


class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'category',
        'price_from',
        'get_photo',
    )
    list_display_links = (
        'id',
        'title',
    )
    list_filter = (
        'title',
    )
    search_fields = (
        'title',
    )
    fields = (
        'title',
        'category',
        'price_from',
        'photo',
    )
    readonly_fields = (
        'get_photo',
    )

    @staticmethod
    def get_photo(obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return 'Фотографии нет'


class LowerBannerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'sale',
        'category',
        'price_from',
        'get_photo',
    )
    list_display_links = (
        'id',
        'title',
    )
    list_filter = (
        'title',
    )
    search_fields = (
        'title',
    )
    fields = (
        'title',
        'category',
        'sale',
        'price_from',
        'photo',
    )
    readonly_fields = (
        'get_photo',
    )

    @staticmethod
    def get_photo(obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return 'Фотографии нет'


admin.site.register(banner.Banner, BannerAdmin)
admin.site.register(lower_banner.LowerBanner, LowerBannerAdmin)
