from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import social_network, our_service, \
    contact, testimonial, logo, our_company


class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'url',
        'photo',
        'get_photo',
    )
    list_display_links = (
        'id',
        'name',
    )
    list_filter = (
        'name',
    )
    search_fields = (
        'name',
        'url',
    )
    fields = (
        'name',
        'photo',
        'url',
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


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'phone',
        'locate',
    )
    list_display_links = (
        'id',
        'email',
        'phone',
    )
    list_filter = (
        'email',
    )
    search_fields = (
        'email',
        'phone',
        'locate',
    )
    fields = (
        'email',
        'phone',
        'locate',
    )


class OurServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'url',
        'photo',
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
        'description',
        'url',
    )
    fields = (
        'title',
        'description',
        'url',
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


class OurCompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'url',
    )
    list_display_links = ('id', 'title',)
    list_filter = ('title',)
    search_fields = (
        'title',
        'url',
    )
    fields = (
        'title',
        'url',
    )


class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'get_photo',
        'position',
        'description',
    )
    list_display_links = (
        'id',
        'name',
    )
    list_filter = (
        'name',
    )
    search_fields = (
        'name',
        'description',
    )
    fields = (
        'name',
        'photo',
        'position',
        'description',
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


class LogoPhotoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_photo',
    )
    list_display_links = (
        'id',
    )
    fields = (
        'photo',
    )

    @staticmethod
    def get_photo(obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return 'Фотографии нет'


admin.site.register(social_network.Network, SocialNetworkAdmin)
admin.site.register(our_service.Service, OurServiceAdmin)
admin.site.register(contact.Contact, ContactAdmin)
admin.site.register(testimonial.Testimonial, TestimonialAdmin)
admin.site.register(logo.Logo, LogoPhotoAdmin)
admin.site.register(our_company.OurCompany, OurCompanyAdmin)