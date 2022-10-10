from shop.models import LowerBanner, Banner


def give_banners():
    return Banner.objects.select_related('category')


def give_lower_banner():
    return LowerBanner.objects.last()
