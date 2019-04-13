from django.db import models
from .product import Product
from .category import Category
# from simple_history.models import HistoricalRecords

class Catalog(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE,
                                                                                verbose_name='Categoria producte')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantitat')

    # Contains all the changes of the object
    # history = HistoricalRecords()


# Aqui el que sols fem es guardar la cantitad del prudcte, pero a la vegada es utilitzar per relaciona la informació del
# producte amb la de la seva categoria, així fent els querrys possibles més sencills i sense trencarnos el cap