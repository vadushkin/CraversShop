from django.core.cache import cache

from shop.models import LowerBanner, Banner


def give_banners():
    query = cache.get('Banner')
    if not query:
        query = Banner.objects.select_related('category')
        cache.set('Banner', query, 300)
    return query


def give_lower_banner():
    query = cache.get('LowerBanner')
    if not query:
        query = LowerBanner.objects.last()
        cache.set('LowerBanner', query, 300)
    return query
