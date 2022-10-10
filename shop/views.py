from django.views.generic import ListView, DetailView

from shop.models.blog import Blog
from shop.models.category import Category
from shop.models.product import Product
from shop.queries import products, categories, services_for_site, banners, blogs
from shop.services import give_dict_with_base_queries


class ShopHome(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'shop/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # todo сделать кеш для большинства запросов

        # title
        context['title'] = 'Cravers'

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
