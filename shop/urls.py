from django.urls import path

from shop.views import ShopHome, ProductsByCategoryListView, ProductDetailView, BlogDetailView

urlpatterns = [
    path('', ShopHome.as_view(), name='home'),

    # static urls
    path('blogs/', ShopHome.as_view(), name='blogs'),
    path('hot-offers/', ShopHome.as_view(), name='hot-offers'),

    # blogs
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog'),

    # categories
    path('category/<slug:slug>/', ProductsByCategoryListView.as_view(), name='posts-by-category'),
    path('categories/<slug:slug>/', ProductsByCategoryListView.as_view(), name='categories'),

    # products
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='products'),
]
