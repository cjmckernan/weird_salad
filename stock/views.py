from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import IngredientForm
from .mixins import LocationIdFilterMixin
from stock.models import Ingredient
from django.contrib.auth.mixins import LoginRequiredMixin




class StockIngredients(LoginRequiredMixin, LocationIdFilterMixin, ListView):
    model = Ingredient
    template_name = 'stock/stock_list.html'

class StockIngredientsCreate(LoginRequiredMixin, LocationIdFilterMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'stock/stock_add.html'
    success_url = reverse_lazy('ingredients')

    def form_valid(self, form):
        ingredient = form.save(commit=False)
        ingredient.location = self.request.user.location
        ingredient.save()
        return super().form_valid(form)

class StockIngredientUpdate(LoginRequiredMixin, LocationIdFilterMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'stock/stock_edit.html'
    success_url = reverse_lazy('ingredients')

class StockIngredientDelete(LoginRequiredMixin, LocationIdFilterMixin, DeleteView):
    model = Ingredient
    template_name = 'stock/stock_delete.html'
    success_url = reverse_lazy('ingredients')
