from django.views.generic import ListView, View
from stock.models import Recipe
from .models import Sale
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import JsonResponse
import json


class SaleCreateView(LoginRequiredMixin, ListView):
    model = Sale
    template_name = 'sales/sale_create.html'
    success_url = reverse_lazy('sale_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_location = self.request.user.location
        context['recipes'] = Recipe.objects.filter(location=user_location)  
        return context

class SaleProcessView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        items = data.get('items', [])
        is_card = data.get('is_card', False) 
        total = data.get('total')
        employee = request.user

        sale = Sale.objects.create(employee=employee, is_card=is_card, total_cost=total, location=employee.location) 

        sale.save()

        return JsonResponse({'success': True, 'redirect_url': reverse_lazy('sale_create')})

class SaleProcessedView(TemplateView):
    template_name = 'sales/sale_processed.html'

