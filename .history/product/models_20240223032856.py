from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80)


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    image = models.ImageField(upload_to='product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_products')

