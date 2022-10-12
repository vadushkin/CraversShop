from django.core.cache import cache

from shop.models import BrandDirectoryCategory, \
    PopularCategory, Category


def give_brand_directory_category():
    query = cache.get('BrandDirectoryCategory')
    if not query:
        query = BrandDirectoryCategory.objects.all().prefetch_related('product')
        cache.set('BrandDirectoryCategory', query, 120)
    return query


def give_popular_category():
    query = cache.get('PopularCategory')
    if not query:
        query = PopularCategory.objects.select_related('category')[:5]
        cache.set('PopularCategory', query, 120)
    return query


def give_category():
    query = cache.get('Category')
    if not query:
        query = Category.objects.all().prefetch_related('children')
        cache.set('Category', query, 120)
    return query
