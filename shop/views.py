from django.db import models
from django.views.generic import ListView, DetailView

from shop.models.blog import Blog
from shop.models.category import Category
from shop.models.product import Product
from shop.queries import products, categories, services_for_site, banners, blogs


def get_mptt_prefetch(field_name, lookup_name='__parent', related_model_qs=None):
    max_level = related_model_qs.values('level').aggregate(max_level=models.Max('level'))['max_level']
    prefetch_list = []
    prefetch_string = field_name
    for i in range(max_level):
        prefetch_string += lookup_name
        prefetch_list.append(prefetch_string)
    return prefetch_list


class ShopHome(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'shop/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # todo сделать кеш для большинства запросов

        # title
        context['title'] = 'Cravers'

        # blogs
        context['blogs'] = blogs.give_blogs()

        # banners
        context['banners'] = banners.give_banners()
        context['lower_banner'] = banners.give_lower_banner()

        # categories
        context['brand_directory_categories'] = categories.give_brand_directory_category()
        context['popular_categories'] = categories.give_popular_category()

        # services for site
        context['networks'] = services_for_site.give_networks()
        context['company'] = services_for_site.give_our_companies()
        context['our_services'] = services_for_site.give_services()
        context['testimonial'] = services_for_site.give_testimonials()
        context['contacts'] = services_for_site.give_contacts()
        context['logo'] = services_for_site.give_logo()

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

        # todo повторюшки

        context['brand_directory_categories'] = categories.give_brand_directory_category()
        context['categories'] = categories.give_category()
        context['company'] = services_for_site.give_our_companies()
        context['our_services'] = services_for_site.give_services()
        context['contacts'] = services_for_site.give_contacts()
        context['popular_categories'] = categories.give_popular_category()
        context['networks'] = services_for_site.give_networks()
        context['logo'] = services_for_site.give_logo()

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

        context['categories'] = categories.give_category()
        context['company'] = services_for_site.give_our_companies()
        context['our_services'] = services_for_site.give_services()
        context['popular_categories'] = categories.give_popular_category()
        context['brand_directory_categories'] = categories.give_brand_directory_category()
        context['networks'] = services_for_site.give_networks()
        context['contacts'] = services_for_site.give_contacts()
        context['logo'] = services_for_site.give_logo()

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

        context['company'] = services_for_site.give_our_companies()
        context['our_services'] = services_for_site.give_services()
        context['brand_directory_categories'] = categories.give_brand_directory_category()
        context['networks'] = services_for_site.give_networks()
        context['categories'] = categories.give_category()
        context['contacts'] = services_for_site.give_contacts()
        context['popular_categories'] = categories.give_popular_category()
        context['logo'] = services_for_site.give_logo()

        return context

    def get_queryset(self):
        queryset = Blog.objects.filter(slug=self.kwargs['slug'])
        return queryset
