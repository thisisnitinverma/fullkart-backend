# urls.py
from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryListView, CategoryDetailView, ProductByCategoryListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/by-category/<slug:slug>/', ProductByCategoryListView.as_view(), name='product-by-category-list'),
    # other paths...
]
