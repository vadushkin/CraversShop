from shop.models import ProductOfTheDay, Product, BestProduct


def give_best_products():
    return BestProduct.objects.all().select_related('product')


def give_products_order_by_created_at():
    return Product.objects.select_related('category').order_by("-created_at")[:12]


def give_products_order_by_updated_at():
    return Product.objects.select_related('category').order_by("-updated_at")[:4]


def give_products_order_by_stars():
    return Product.objects.select_related('category').order_by("-stars")[:4]


def give_products_order_by_price():
    return Product.objects.select_related('category').order_by("-price")[:4]


def give_product_of_the_day():
    return ProductOfTheDay.objects.filter(open=True).select_related('product').order_by("-created_at").last()
