from django.contrib.auth.views import LoginView

class EmployeeLogin(LoginView):
    template_name = "employee/login.html"
