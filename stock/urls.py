from django.urls import path
from stock.views import (
    RecipeDeleteView,
    RecipeListView,
    StockIngredients,
    StockIngredientsCreate,
    StockIngredientUpdate,
    StockIngredientDelete,
    RecipeCreatorView,
    recipe_create,
)

urlpatterns = [
    path('ingredients', StockIngredients.as_view(), name='ingredients'),
    path('ingredients_add', StockIngredientsCreate.as_view(), name='ingredient_add'),
    path('ingredient_edit/<int:pk>/', StockIngredientUpdate.as_view(), name='ingredient_edit'),
    path('ingredient_delete/<int:pk>/', StockIngredientDelete.as_view(), name='ingredient_delete'),
    path('recipe_creator', RecipeCreatorView.as_view(), name='recipe_creator'),
    path('recipe/create/', recipe_create, name='recipe_create'),
    path('recipes', RecipeListView.as_view(), name='recipe_list'),\
    path('recipes/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),

]
