from django.db import models
from employee.models import Location

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=256)
    quantity = models.DecimalField(max_digits=9, decimal_places=3, default=0.000)
    location = models.ForeignKey(Location, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('ingredient_name', 'location')

    def __str__(self):
        return self.ingredient_name


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    location = models.ForeignKey(Location,  null=True, on_delete=models.DO_NOTHING) 
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 

    class Meta:
        unique_together = ('name', 'location')

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=9, decimal_places=3, default=0.000)

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.ingredient_name} in {self.recipe.name}"
