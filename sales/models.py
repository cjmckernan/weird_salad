from django.db import models
from employee.models import Employee, Location

class Sale(models.Model):
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    is_card = models.BooleanField(default=False)
    employee = models.ForeignKey(Employee, null=True, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.total_cost)
