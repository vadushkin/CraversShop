from shop.models import Blog


def give_blogs():
    return Blog.objects.select_related('category').select_related('author').order_by("-created_at")[:4]
