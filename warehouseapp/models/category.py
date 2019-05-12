from django.db import models


class Category(models.Model):

    STR_PATTERN = "Categoria: {} Tipus:{} Departament: {}"

    category = models.CharField(max_length=32, default='None')
    department_type = models.CharField(max_length=32, default='None')
    department = models.CharField(max_length=32, default='None')

    def __str__(self):
        return Category.STR_PATTERN.format(self.category, self.department_type, self.department)

# La explicació es la següent: per a poder realitzar la llista de querrys fixos depenent del
# departament y altres coses hem de tenir un identificador que ens doni tot del producte, ja que sino sera impossible
# organitzar la informació que tenim en el Amazon API. per aixo he optat que les categories sorganitcin aixi: primer
# sera la categoria especifica: Si es RAM, targeta grafica, microprocessador de mobil, pistò, etc.
# Despres sera la succeció del departament: si es Ordinadors, Mobils o TVs, i per acabar seran un dels dos departaments:
# Informatica o Electronica. D'aquesta forma estara organitzat en columnes que van de més probabilitat de fer querry
# (category) a menos probabilitat (departament o de informatica o de electronica)
