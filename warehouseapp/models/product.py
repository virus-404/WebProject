from django.db import models
from .category import Category


class Product(models.Model):

    STR_PATTERN = "Producte: {} Categoria:{} Unitats: {}"

    product_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, related_name='category_product', on_delete=models.PROTECT, null=True,
                                    verbose_name='Categoria producte')
    name = models.CharField(max_length=128, default='None')
    brand = models.CharField(max_length=16, default='None')
    model = models.CharField(max_length=32, default='None')
    description = models.CharField(max_length=64, default='None')
    product_type = models.CharField(max_length=64, default='None')

    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantitat')

    def __str__(self):
        return Product.STR_PATTERN.format(self.product_id, self.name, self.category_id, self.quantity)


# El problema principal d'aquesta base de dades es "Com creem una base de dades que organitzi tots els productes per
# tipus y subtipus? Estil una base de dades que organitci la ram per DDR3 o DDR4 y a la vegada per micrprocessadors amb
# la seva latencia?" La resposta es que no ho fem per la base de dades, sino per com introduirem en el futur les dades
# a aquesta. Per exemple, Si tenim una ram de DDR$, no ficarem que sigui una ram com a tal en "model", sino que
# especificarem el DDR4. si el microprocessador es un i5, aixo ho ficarem a model. Pero, el problema ve a informaciño
# adicional que de normal especifica de cada part. Aqui es on entre el cam de tipus de producte, el cual la unica
# utilitat que te és de ser capazos de introduir aquesta informació util del producte sense destrozar la base de dades
