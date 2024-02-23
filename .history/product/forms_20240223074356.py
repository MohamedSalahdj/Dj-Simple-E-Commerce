from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = False

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
