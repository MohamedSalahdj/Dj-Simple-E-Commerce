from django.urls import path
from .views import list_products, list_categories, new_product

urlpatterns = [
    path('', list_products, name='list_products'),
    path('category', list_categories, name='list_categories'),
    path('newproduct/', new_product, name='new_product')
]
