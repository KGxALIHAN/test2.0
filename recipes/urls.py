from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeDeleteView, IngredientCreateView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_list'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
    path('ingredient/create/', IngredientCreateView.as_view(), name='ingredient_create'),
]
