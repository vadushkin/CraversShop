from django.urls import path, include
from rest_framework import routers

from shop.views import ShopHome, ProductsByCategoryListView, ProductDetailView, \
    BlogDetailView, cart, checkout, updateItem, BlogsView
from .api import *

router = routers.SimpleRouter()

# products
router.register(r'products', ProductViewSet)
router.register(r'best_products', BestProductViewSet)
router.register(r'products_of_the_day', ProductOfTheDayViewSet)

# blogs
router.register(r'blogs', BlogViewSet)

# categories
router.register(r'categories', CategoryViewSet)
router.register(r'popular_categories', PopularCategoryViewSet)

# customer
router.register(r'customers', CustomerViewSet)


urlpatterns = [
    # home
    path('', ShopHome.as_view(), name='home'),

    # static urls
    path('blogs/', BlogsView.as_view(), name='blogs'),
    path('hot-offers/', ShopHome.as_view(), name='hot-offers'),

    # blogs
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog'),

    # categories
    path('category/<slug:slug>/', ProductsByCategoryListView.as_view(), name='posts-by-category'),

    # products
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product'),

    # cart
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('update_item/', updateItem, name="update_item"),

    # api
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls'))
]
