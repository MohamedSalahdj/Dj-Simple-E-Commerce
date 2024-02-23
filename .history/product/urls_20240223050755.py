from django.urls import path
from .views import list_categories, list_products, new_product, product_details, edit_product

urlpatterns = [
    path('category', list_categories, name='list_categories'),
    path('', list_products, name='list_products'),
    path('newproduct/', new_product, name='new_product'),
    path('product/<int:product_id>', product_details, name='product_details'),
    path('product/<int:product_id>/edit', edit_product, name='edit_product'),
]
