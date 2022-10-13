from rest_framework import viewsets

from .serializers import *


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductOfTheDayViewSet(viewsets.ModelViewSet):
    queryset = ProductOfTheDay.objects.all()
    serializer_class = ProductOfTheDaySerializer


class BestProductViewSet(viewsets.ModelViewSet):
    queryset = BestProduct.objects.all()
    serializer_class = BestProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PopularCategoryViewSet(viewsets.ModelViewSet):
    queryset = PopularCategory.objects.all()
    serializer_class = PopularCategorySerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
