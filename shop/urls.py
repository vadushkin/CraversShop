from django.urls import path

from shop.views import home_page

urlpatterns = [
    path('', home_page, name='home')
]
