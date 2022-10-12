from django.core.cache import cache

from shop.models import Contact, Logo, Testimonial, Network, OurCompany, Service


def give_contacts():
    query = cache.get('Contact')
    if not query:
        query = Contact.objects.all()
        cache.set('Contact', query, 300)
    return query


def give_logo():
    query = cache.get('Logo')
    if not query:
        query = Logo.objects.last()
        cache.set('Logo', query, 300)
    return query


def give_testimonials():
    query = cache.get('Testimonial')
    if not query:
        query = Testimonial.objects.last()
        cache.set('Testimonial', query, 300)
    return query


def give_networks():
    query = cache.get('Network')
    if not query:
        query = Network.objects.all()[:5]
        cache.set('Network', query, 300)
    return query


def give_our_companies():
    query = cache.get('OurCompany')
    if not query:
        query = OurCompany.objects.all()[:5]
        cache.set('OurCompany', query, 300)
    return query


def give_services():
    query = cache.get('Service')
    if not query:
        query = Service.objects.all()[:5]
        cache.set('Service', query, 300)
    return query
