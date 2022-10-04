from django.views.generic import ListView

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


class CategoryListView(ListView):
    model = Category
    template_name = 'shop/category.html'


# class PostByCategoryView(ListView):
#     context_object_name = 'posts'
#     template_name = 'shop/post.html'
#
#     def get_queryset(self):
#         self.category = Category.objects.get(slug=self.kwargs['slug'])
#         queryset = Post.objects.filter(category=self.category)
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = self.category
#         return context
