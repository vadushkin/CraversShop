from django.shortcuts import render

from shop.models.social_networks import Network


def home_page(request):
    networks = Network.objects.all()
    context = {
        'title': 'Главная',
        'networks': networks,
    }
    return render(request, 'shop/home.html', context=context)
