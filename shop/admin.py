from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import social_networks


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


admin.site.register(social_networks.Network, SocialNetworkAdmin)
