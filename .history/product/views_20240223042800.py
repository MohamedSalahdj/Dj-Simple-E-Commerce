from django.shortcuts import render
from .models import Category, Product
from .forms import ProductForm

def list_categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    return render (request, 'product/category/list_category.html', context)


def list_products(request):
    products = Product.objects.all()

    return render(request, 'product/product/list_products.html', {'products':products})



def new_product(request):

    if request.method == 'POST':
        product_form =  ProductForm(request.POST, request.FILES)

    else:
        product_form = ProductForm()

    context = {'form' : product_form}

    return render(request, 'product/product/new_product.html', context)
