from django.urls import path
from .views import (
    RecipeListView, RecipeDetailView, RecipeCreateView, RecipeImageCreateView
)
urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe-add'),
    path(
        'recipe/<int:pk>/add_image', 
        RecipeImageCreateView.as_view(), 
        name='recipe-image-add'
    )
]

app_name = "ledger"
