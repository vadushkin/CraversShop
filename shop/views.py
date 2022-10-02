from django.views.generic import ListView, DetailView

from shop.models.category import Category
from shop.models.social_network import Network


class ShopHome(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'shop/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cravers'
        context['networks'] = Network.objects.all()
        return context


class CategoryView(DetailView):
    template_name = 'shop/category.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
