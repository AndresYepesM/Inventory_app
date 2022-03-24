from django import forms
from product.models import Items

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = [
            'name',
            'detail',
            'price',
            'quantity'
        ]