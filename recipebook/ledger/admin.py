from django.contrib import admin
from .models import Recipe, RecipeIngredient
# Register your models here.


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine,]


admin.site.register(Recipe, RecipeAdmin)
