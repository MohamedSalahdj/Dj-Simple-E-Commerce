from django.urls import path
from .views import list_products, list_categories, new_product, edit_product

urlpatterns = [
    path('', list_products, name='list_products'),
    path('category', list_categories, name='list_categories'),
    path('newproduct/', new_product, name='new_product'),
    path('product/<int:product_id>/edit', edit_product, name='edit_product'),
]
