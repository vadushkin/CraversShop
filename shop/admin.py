from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import social_network, category


class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'url', 'photo', 'get_photo')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name', 'url')
    fields = ('name',
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


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'slug', 'photo', 'get_photo')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'slug', )
    search_fields = ('name', 'slug', )
    prepopulated_fields = {'slug': ('name',), }
    fields = ('name',
              'slug',
              'photo',
              )
    readonly_fields = ('get_photo',)

    @staticmethod
    def get_photo(obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return 'Фотографии нет'


admin.site.register(social_network.Network, SocialNetworkAdmin)
admin.site.register(category.Category, CategoryAdmin)
