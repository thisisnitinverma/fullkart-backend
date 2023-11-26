# views.py
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.generics import get_object_or_404
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .pagination import OffsetLimitPagination  
from rest_framework.filters import SearchFilter

class SlugRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    def get_object(self):
        queryset = self.get_queryset()
        slug_field = self.slug_field
        slug = self.kwargs[slug_field]
        return get_object_or_404(queryset, **{slug_field: slug})

class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = OffsetLimitPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']  # Add more fields if needed

    # Override the get_queryset method to customize the search behavior
    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.request.query_params.get('category_slug', None)

        # Filter by category if provided
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)

        return queryset


class ProductDetailView(SlugRetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    slug_field = 'slug'

class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = OffsetLimitPagination 

class CategoryDetailView(SlugRetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    slug_field = 'slug'

class ProductByCategoryListView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = OffsetLimitPagination 

    def get_queryset(self):
        category_slug = self.kwargs['slug']
        category = get_object_or_404(Category, slug=category_slug)
        return Product.objects.filter(category=category)
