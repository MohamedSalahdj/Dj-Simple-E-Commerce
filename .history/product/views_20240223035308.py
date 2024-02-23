from django.shortcuts import render
from .models import Category, Product


def list_products(request):
    products = Product.objects.all()

    return render(request, 'product/list_products.html', {'products':products})
