from django import template

register = template.Library()


@register.filter
def sale_price(price: int, sale: int) -> str:
    """Возвращает цену со скидкой"""
    try:
        price -= price * sale / 100
    except:
        pass
    return format(price, '.2f')


@register.filter
def give_another_stars(stars: int) -> range:
    """Возвращает остающиеся звезды"""
    try:
        stars = 5 - int(stars)
    except:
        pass
    return range(stars)


@register.filter
def give_range_stars(stars: int) -> range:
    """Возвращает все звезды"""
    try:
        return range(int(stars))
    except:
        pass
