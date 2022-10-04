from django.urls import path

from shop.views import ShopHome, CategoryListView, ProductDetailView

urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('category/<str:slug>/', CategoryListView.as_view(), name='posts-by-category'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='product'),
]
