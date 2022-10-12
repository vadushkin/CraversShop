from django.core.cache import cache

from shop.models import ProductOfTheDay, Product, BestProduct


def give_best_products():
    query = cache.get('BestProduct')
    if not query:
        query = BestProduct.objects.all().select_related('product')
        cache.set('BestProduct', query, 120)
    return query


def give_products_order_by_created_at():
    query = cache.get('ProductCreated_at')
    if not query:
        query = Product.objects.select_related('category').order_by("-created_at")[:12]
        cache.set('ProductCreated_at', query, 30)
    return query


def give_products_order_by_updated_at():
    query = cache.get('ProductUpdated_at')
    if not query:
        query = Product.objects.select_related('category').order_by("-updated_at")[:4]
        cache.set('ProductUpdated_at', query, 30)
    return query


def give_products_order_by_stars():
    query = cache.get('ProductStars')
    if not query:
        query = Product.objects.select_related('category').order_by("-stars")[:4]
        cache.set('ProductStars', query, 180)
    return query


def give_products_order_by_price():
    query = cache.get('ProductPrice')
    if not query:
        query = Product.objects.select_related('category').order_by("-price")[:4]
        cache.set('ProductPrice', query, 150)
    return query


def give_product_of_the_day():
    query = cache.get('ProductOfTheDay')
    if not query:
        query = ProductOfTheDay.objects.filter(open=True).select_related('product').order_by("-created_at").last()
        cache.set('ProductOfTheDay', query, 300)
    return query
