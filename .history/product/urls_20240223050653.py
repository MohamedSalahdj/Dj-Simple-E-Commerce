from django.urls import path
from .views import list_products, list_categories, new_product, product_details,edit_product

urlpatterns = [
    path('category', list_categories, name='list_categories'),
    path('', list_products, name='list_products'),
    path('newproduct/', new_product, name='new_product'),
    path(),
    path('product/<int:product_id>/edit', edit_product, name='edit_product'),
]
