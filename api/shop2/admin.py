from django import forms
from django.contrib import admin
from .models import Product, Category, Image

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'category': forms.Select(attrs={'class': 'select2'}),  # You can style the select field using a library like Select2
        }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('title', 'price', 'category', 'slug')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('url',)

