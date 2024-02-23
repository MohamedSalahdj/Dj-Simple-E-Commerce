from django.db import models

class Category(models.Model):
    name = 


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    image = models.ImageField(upload_to='product')

