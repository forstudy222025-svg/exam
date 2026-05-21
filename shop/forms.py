from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']
        labels = {
            'name': 'Product Name',
            'description': 'Description',
            'price': 'Price',
            'stock': 'Stock Quantity',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter product name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter product description', 'rows': 4}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter price'}),
            'stock': forms.NumberInput(attrs={'placeholder': 'Enter stock quantity'}),
        }
