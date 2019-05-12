from django import forms
from warehouseapp.models import Product, Category


class NewProductForm(forms.ModelForm):
    name = forms.CharField(max_length=64, required=True)
    category_id = forms.ChoiceField(required=False)  # Falta acabar-ho
    category_id = Category.category
    brand = forms.CharField(max_length=16, required=False)
    model = forms.CharField(max_length=32, required=False)
    description = forms.CharField(max_length=64, required=False)
    product_type = forms.CharField(max_length=64, required=False)
    quantity = forms.IntegerField(required=True, min_value=0)  # Afegir comprovacio que sigui mes gran q 0

    class Meta:
        model = Product
        fields = ('category_id', 'name', 'brand', 'model', 'description', 'product_type', 'quantity',)
        exclude = ('product_id',)
