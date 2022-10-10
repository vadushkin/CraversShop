from shop.queries import categories, services_for_site


def give_dict_with_base_queries(context: dict) -> dict | None:
    """
    Context is a list from a view.
    Returns a dictionary with base queries.
    """

    if dict is None:
        return None

    # categories
    context['brand_directory_categories'] = categories.give_brand_directory_category()
    context['popular_categories'] = categories.give_popular_category()
    context['categories'] = categories.give_category()

    # services for site
    context['company'] = services_for_site.give_our_companies()
    context['our_services'] = services_for_site.give_services()
    context['contacts'] = services_for_site.give_contacts()
    context['networks'] = services_for_site.give_networks()
    context['testimonial'] = services_for_site.give_testimonials()
    context['logo'] = services_for_site.give_logo()

    return context
