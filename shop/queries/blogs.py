from shop.models import Blog
from django.core.cache import cache


def give_blogs():
    query = cache.get('Blog')
    if not query:
        query = Blog.objects.select_related('category').select_related('author').order_by("-created_at")[:4]
        cache.set('Blog', query, 90)
    return query
