# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<slug:slug>/', views.ProductRetrieveUpdateDeleteView.as_view(), name='product-retrieve-update-delete'),
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<slug:slug>/', views.CategoryRetrieveUpdateDeleteView.as_view(), name='category-retrieve-update-delete'),
]
