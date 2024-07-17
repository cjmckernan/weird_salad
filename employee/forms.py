from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Employee 

class EmployeeCreationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = (
            "username",
            "email",
            "location",
            "edit_stock",
            "take_payments",
        )

class EmployeeChangeForm(UserChangeForm):
    class Meta:
        model = Employee 
        fields = (
            "username",
            "email",
            "location",
            "edit_stock",
            "take_payments",
        )
