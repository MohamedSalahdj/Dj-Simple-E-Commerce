from django.urls import path
from .views import list_products, list_categories

urlpatterns = [
    path('', list_products, name='list_products'),
]
