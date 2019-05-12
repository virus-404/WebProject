from django.db import models
from .product import Product
from .category import Category
from datetime import date
# from simple_history.models import HistoricalRecords


class CatalogChange(models.Model):

    STR_PATTERN = "Producte: {} Categoria:{} Unitats Modificades: {}"

    product_id_change = models.ForeignKey(Product, related_name='product_id_change', on_delete=models.SET_NULL, null=True, verbose_name='Producte')
    category_id_change = models.ForeignKey(Category, related_name='category_product_change', on_delete=models.SET_NULL, null=True,
                                                                                verbose_name='Categoria producte')
    quantity_modify = models.PositiveIntegerField(default=0, verbose_name='Quantitat modificada')

    date = models.DateField(default=date.today)

    # Contains all the changes of the object
    # history = HistoricalRecords()


    def __str__(self):
        return CatalogChange.STR_PATTERN.format(self.product_id_change, self.category_id_change, self.quantity_modify)

# Aqui el que sols fem es guardar la cantitad del prudcte, pero a la vegada es utilitzar per relaciona la informació del
# producte amb la de la seva categoria, així fent els querrys possibles més sencills i sense trencarnos el cap

