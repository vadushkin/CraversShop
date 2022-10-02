from django.urls import path

from shop.views import ShopHome, CategoryView

urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('category/<slug:slug>', CategoryView.as_view, name='category'),
]
