from django.shortcuts import render
from .models import Category, Product


def list_categories(request):
    categories = Category.objects.all()

    return render (request, 'product/category/list_category.html')


def list_products(request):
    products = Product.objects.all()

    return render(request, 'product/product/list_products.html', {'products':products})


