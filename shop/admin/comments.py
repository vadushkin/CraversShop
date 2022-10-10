from django.contrib import admin

from shop.models import comment


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
        'blog',
        'author',
        'created_at',
    )
    list_display_links = (
        'id',
    )
    list_filter = (
        'text',
    )
    search_fields = (
        'text',
        'author',
    )
    fields = (
        'text',
        'blog',
    )
    readonly_fields = (
        'created_at',
    )


admin.site.register(comment.Comment, CommentAdmin)
