from django.urls import path
from .views import list_categories, category_details, new_category, edit_category, list_products, new_product, product_details, edit_product, delete_product

urlpatterns = [
    path('', list_products, name='list_products'),
    path('category', list_categories, name='list_categories'),
    path('newcateory', new_category, name='new_category'),
    path('category/<int:category_id>', category_details, name='category_details'),
    path('category/<int:category_id>/edit', ),
    path('newproduct/', new_product, name='new_product'),
    path('product/<int:product_id>', product_details, name='product_details'),
    path('product/<int:product_id>/edit', edit_product, name='edit_product'),
    path('product/<int:product_id>/delete', delete_product, name='delete_product'),

]
