from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='product')