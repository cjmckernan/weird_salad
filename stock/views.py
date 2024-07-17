from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import IngredientForm
from .mixins import LocationIdFilterMixin
from stock.models import Ingredient
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




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

class RecipeCreatorView(LoginRequiredMixin, LocationIdFilterMixin, ListView):
    model = Ingredient
    template_name = 'stock/stock_recipe_create.html'
    success_url = reverse_lazy('ingredients')

from django.shortcuts import render, redirect
from .models import Recipe, Ingredient, RecipeIngredient
from django.contrib.auth.decorators import login_required

@login_required
def recipe_create(request):
    if request.method == 'POST':
        recipe_name = request.POST['name']
        ingredient_ids = request.POST.getlist('ingredients[]')
        quantities = request.POST.getlist('quantities[]')

        user_location = request.user.location

        recipe = Recipe.objects.create(name=recipe_name, location=user_location)

        for ingredient_id, quantity in zip(ingredient_ids, quantities):
            ingredient = Ingredient.objects.get(id=ingredient_id)
            quantity_in_kg = float(quantity) / 1000  # Convert grams to kilograms
            RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient, quantity=quantity_in_kg)

        return redirect('ingredients')  # Adjust this to your success URL

    ingredients = Ingredient.objects.all()
    return render(request, 'stock/stock_recipe_create.html', {'object_list': ingredients})




class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'stock/stock_recipe_list.html'
    context_object_name = 'recipes'

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'stock/stock_recipe_delete.html'
    success_url = reverse_lazy('recipe_list')
