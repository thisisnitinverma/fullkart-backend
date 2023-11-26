from rest_framework import serializers
from .models import Product, Category, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('url',)

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='slug')
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'description', 'category', 'images', 'slug')

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])  # Get the data for images, default to an empty list
        product = Product.objects.create(**validated_data)

        # Create Image objects for each image data and associate them with the product
        for image_data in images_data:
            Image.objects.create(product=product, **image_data)

        return product

    def get_images(self, product):
        # Get a list of image URLs for the product
        image_urls = [image.url for image in product.images.all()]
        return image_urls

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'slug')
