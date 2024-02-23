from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import CategoryForm, ProductForm 

def list_categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    return render (request, 'product/category/list_category.html', context)


def category_details(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)

    context = {
        'category' : category,
        'products' : products
    }

    return render(request, 'product/category/category_details.html', context)

def new_category(request):
    form = CategoryForm()

def list_products(request):
    products = Product.objects.all()

    return render(request, 'product/product/list_products.html', {'products':products})



def new_product(request):
    if request.method == 'POST':
        product_form =  ProductForm(request.POST, request.FILES)
        if product_form.is_valid() :
            product_form.save() 
            return redirect('/')
    else:
        product_form = ProductForm()

    context = {'form' : product_form}

    return render(request, 'product/product/new_product.html', context)

def product_details(request, product_id):

    product = Product.objects.get(id=product_id)
    context = {'product':product}
    
    return render(request, 'product/product/product_details.html', context)


def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product_form =  ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid() :
            product_form.save() 
            return redirect('/')
    else:
        product_form = ProductForm(instance=product)

    context = {'form' : product_form}

    return render(request, 'product/product/edit_product.html', context)


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('/')

