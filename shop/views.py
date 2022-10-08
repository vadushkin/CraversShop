from django.views.generic import ListView, DetailView

from shop.models import Banner
from shop.models.best_product import BestProduct
from shop.models.blog import Blog
from shop.models.category import Category
from shop.models.contact import Contact
from shop.models.our_company import OurCompany
from shop.models.our_service import Service
from shop.models.product import Product
from shop.models.product_of_the_day import ProductOfTheDay
from shop.models.social_network import Network


class ShopHome(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'shop/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # todo сделать кеш для большинства запросов
        contacts = Contact.objects.last()
        context['title'] = 'Cravers'
        if contacts:
            context['phone'] = contacts.phone
            context['email'] = contacts.email
            context['locate'] = contacts.locate
        context['blogs'] = Blog.objects.select_related('category').select_related('author').order_by("-created_at")[:4]
        context['banners'] = Banner.objects.select_related('category')
        context['networks'] = Network.objects.all()[:5]
        context['company'] = OurCompany.objects.all()[:5]
        context['our_services'] = Service.objects.all()[:5]
        context['best_product'] = BestProduct.objects.all().select_related('product')
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


class BlogDetailView(DetailView):
    context_object_name = 'blog'
    template_name = 'shop/blog.html'

    def get_queryset(self):
        queryset = Blog.objects.filter(slug=self.kwargs['slug'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs["slug"].title()
        return context
