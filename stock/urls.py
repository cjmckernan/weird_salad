from django.urls import path

from stock.views import StockIngredients, StockIngredientsCreate, StockIngredientUpdate, StockIngredientDelete

urlpatterns = [
    path('ingredients', StockIngredients.as_view(), name='ingredients'),
    path('ingredients_add', StockIngredientsCreate.as_view(), name='ingredient_add'),
    path('ingredient_edit/<int:pk>/', StockIngredientUpdate.as_view(), name='ingredient_edit'),
    path('ingredient_delete/<int:pk>/', StockIngredientDelete.as_view(), name='ingredient_delete'),
]
