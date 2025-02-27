from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
