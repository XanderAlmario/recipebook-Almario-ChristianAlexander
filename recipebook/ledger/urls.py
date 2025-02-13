from django.urls import path
from .views import RecipeList, Recipe1, Recipe2

urlpatterns = [
    path('recipes/list', RecipeList, name='Recipe List'),
    path('recipe/1', Recipe1, name='Recipe 1'),
    path('recipe/2', Recipe2, name='Recipe 2'),
]

app_name = "ledger"