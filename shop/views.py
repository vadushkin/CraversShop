import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from shop.models.blog import Blog
from shop.models.category import Category
from shop.models.product import Product
from shop.queries import products, categories, banners, blogs
from shop.services import give_dict_with_base_queries
from .models import Order, OrderItem
from .utils import cartData


class ShopHome(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'shop/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # title
        context['title'] = 'Cravers'

        data = cartData(self.request)

        cartItems = data['cartItems']
        product = Product.objects.all()

        # items
        context['cartItems'] = cartItems
        context['products'] = product

        # added base queries
        give_dict_with_base_queries(context)

        # blogs
        context['blogs'] = blogs.give_blogs()

        # banners
        context['banners'] = banners.give_banners()
        context['lower_banner'] = banners.give_lower_banner()

        # products
        context['best_product'] = products.give_best_products()
        context['last_products'] = products.give_products_order_by_created_at()
        context['new_products'] = products.give_products_order_by_updated_at()
        context['top_rated_products'] = products.give_products_order_by_stars()
        context['most_expensive_products'] = products.give_products_order_by_price()
        context['product_of_the_day'] = products.give_product_of_the_day()

        return context

    def get_queryset(self):
        return categories.give_category()


class ProductsByCategoryListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs["slug"].title()
        give_dict_with_base_queries(context)
        return context

    def get_queryset(self):
        queryset = Product.objects.filter(category__slug=self.kwargs['slug'])
        return queryset


class ProductDetailView(DetailView):
    context_object_name = 'product'
    template_name = 'shop/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs["slug"].title()
        give_dict_with_base_queries(context)
        return context

    def get_queryset(self):
        queryset = Product.objects.filter(slug=self.kwargs['slug'])
        return queryset


class BlogDetailView(DetailView):
    context_object_name = 'blog'
    template_name = 'shop/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs["slug"].title()
        give_dict_with_base_queries(context)
        return context

    def get_queryset(self):
        queryset = Blog.objects.filter(slug=self.kwargs['slug'])
        return queryset


class BlogsView(ListView):
    context_object_name = 'blogs'
    template_name = 'shop/blogs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blogs'
        give_dict_with_base_queries(context)
        return context

    def get_queryset(self):
        queryset = Blog.objects.all().select_related('category').select_related('author')
        return queryset


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items.select_related('product'),
        'order': order,
        'cartItems': cartItems,
        'title': 'Cart',
    }
    give_dict_with_base_queries(context)
    return render(request, 'shop/cart.html', context)


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items.select_related('product'),
        'order': order,
        'cartItems': cartItems,
        'title': 'Checkout',
    }
    give_dict_with_base_queries(context)
    return render(request, 'shop/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
