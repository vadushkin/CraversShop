from django import template

register = template.Library()


@register.filter
def sale_price(price: int, sale: int) -> str:
    """
    Give the price at a discount
    """

    try:
        price -= price * sale / 100
    except TypeError:
        pass
    return format(price, '.2f')


@register.filter
def give_another_stars(stars: int) -> range:
    """
    Give away the rest of the stars
    """

    try:
        stars = 5 - int(stars)
    except ValueError:
        pass
    return range(stars)


@register.filter
def give_range_stars(stars: int) -> range:
    """
    Give all stars
    """

    try:
        return range(int(stars))
    except TypeError or ValueError:
        pass


@register.filter
def give_percent(quantity: int, sold: int) -> int:
    """
    Give the percent from the number
    """

    try:
        if sold is None:
            return 1 * 100 // quantity
        return sold * 100 // quantity
    except ZeroDivisionError:
        pass
