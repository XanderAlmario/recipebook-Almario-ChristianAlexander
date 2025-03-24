from django.contrib import admin
from .models import Recipe, RecipeIngredient, RecipeImage, Ingredient
# Register your models here.


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine, RecipeImageInLine,]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
