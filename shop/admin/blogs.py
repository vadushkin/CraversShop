from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'text',
        'author',
        'category',
        'get_photo',
        'stars',
        'likes',
        'created_at',
        'updated_at',
    )
    prepopulated_fields = {
        'slug': ('title',),
    }
    list_display_links = (
        'id',
        'title',
    )
    list_filter = (
        'title',
        'slug',
        'text',
    )
    search_fields = (
        'title',
        'text',
        'author',
    )
    fields = (
        'title',
        'slug',
        'text',
        'stars',
        'category',
        'photo',
    )
    readonly_fields = (
        'get_photo',
        'created_at',
        'updated_at',
    )

    def save_model(self, request, obj, form, change):
        """Переопределяем метод сохранения модели """
        if not change:
            obj.author = request.user

        super(BlogAdmin, self).save_model(
            request=request,
            obj=obj,
            form=form,
            change=change
        )

    @staticmethod
    def get_photo(obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return 'Фотографии нет'


admin.site.register(blog.Blog, BlogAdmin)
