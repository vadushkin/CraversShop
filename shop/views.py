from django.views.generic import ListView, DetailView

from shop.models.category import Category
from shop.models.product import Product
from shop.models.product_of_the_day import ProductOfTheDay
from shop.models.social_network import Network


class ShopHome(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'shop/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cravers'
        context['networks'] = Network.objects.all()[:5]
        context['last_products'] = Product.objects.select_related('category').order_by("-created_at")[:12]
        context['new_products'] = Product.objects.select_related('category').order_by("-updated_at")[:4]
        context['top_rated_products'] = Product.objects.select_related('category').order_by("-stars")[:4]
        context['most_expensive_products'] = Product.objects.select_related('category').order_by("-price")[:4]
        context['product_of_the_day'] = (
            ProductOfTheDay.objects.filter(open=True).select_related('product').order_by("-created_at").last())
        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'shop/category.html'


class ProductDetailView(DetailView):
    context_object_name = 'product'
    template_name = 'shop/post.html'

    def get_queryset(self):
        queryset = Product.objects.filter(slug=self.kwargs['slug'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs["slug"].title()
        return context
