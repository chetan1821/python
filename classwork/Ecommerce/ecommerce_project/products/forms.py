from django import forms
from .models import Product, ProductImage


class ProductFilterForm(forms.Form):
    """
    Form for filtering products.
    """
    search = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search products...'
        })
    )
    
    sort_by = forms.ChoiceField(
        choices=[
            ('', 'Sort By'),
            ('-created_at', 'Newest'),
            ('name', 'Name: A to Z'),
            ('-name', 'Name: Z to A'),
            ('price', 'Price: Low to High'),
            ('-price', 'Price: High to Low'),
        ],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    
    price_min = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Min Price'
        })
    )
    
    price_max = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Max Price'
        })
    )
