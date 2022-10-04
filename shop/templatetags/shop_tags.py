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
