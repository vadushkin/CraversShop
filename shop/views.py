from django.shortcuts import render


def home_page(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'shop/home.html', context=context)
