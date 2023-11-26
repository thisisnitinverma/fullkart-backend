# serializers.py
from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'slug')

class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'description', 'category', 'images', 'slug')
