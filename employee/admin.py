from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Location
from .forms import EmployeeCreationForm, EmployeeChangeForm 

class CustomUserAdmin(UserAdmin):
    add_form = EmployeeCreationForm
    form = EmployeeChangeForm
    list_display = [
        "username",
        "email",
        "location",
        "edit_stock",
        "take_payments",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                "location",
                "edit_stock",
                "take_payments",
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                "location",
                "edit_stock",
                "take_payments",
                )
            },
        ),
    )

admin.site.register(Employee, CustomUserAdmin)
admin.site.register(Location)
