from django.contrib import admin
from .models import Recipe, RecipeIngredient, RecipeImage
# Register your models here.


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine, RecipeImageInLine,]


admin.site.register(Recipe, RecipeAdmin)
