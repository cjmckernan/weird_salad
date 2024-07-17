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



