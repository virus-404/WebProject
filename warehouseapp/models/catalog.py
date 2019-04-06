from django.db import models
from .product import Product
from .category import Category

class Catalog(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

# Aqui el que sols fem es guardar la cantitad del prudcte, pero a la vegada es utilitzar per relaciona la informació del
# producte amb la de la seva categoria, així fent els querrys possibles més sencills i sense trencarnos el cap