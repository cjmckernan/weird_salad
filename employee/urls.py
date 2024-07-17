from django.urls import path
from .views import EmployeeLogin

urlpatterns = [
    path("login/", EmployeeLogin.as_view(), name="login")
]
