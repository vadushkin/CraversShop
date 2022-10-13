from rest_framework import serializers

from .models import Product, ProductOfTheDay, BestProduct, \
    Customer, Category, PopularCategory, Blog


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductOfTheDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOfTheDay
        fields = '__all__'


class BestProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestProduct
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PopularCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularCategory
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
