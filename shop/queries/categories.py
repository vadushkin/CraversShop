from shop.models import BrandDirectoryCategory, \
    PopularCategory, Category


def give_brand_directory_category():
    return BrandDirectoryCategory.objects.all().prefetch_related('product')


def give_popular_category():
    return PopularCategory.objects.select_related('category')[:5]


def give_category():
    return Category.objects.all().prefetch_related('children')
