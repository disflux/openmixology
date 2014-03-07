from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    abv = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=16, null=True, blank=True)
    
class Recipe(models.Model):
    name = models.CharField(max_length=64)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeItem')
    
class RecipeItem(models.Model):

    UNIT_CHOICES = (
        ('oz', 'Ounces'),
    )
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=4, choices=UNIT_CHOICES)
    
