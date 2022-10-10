from shop.models import Contact, Logo, Testimonial, Network, OurCompany, Service


def give_contacts():
    return Contact.objects.all()


def give_logo():
    return Logo.objects.last()


def give_testimonials():
    return Testimonial.objects.last()


def give_networks():
    return Network.objects.all()[:5]


def give_our_companies():
    return OurCompany.objects.all()[:5]


def give_services():
    return Service.objects.all()[:5]
