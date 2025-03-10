from django.contrib import admin
from .models import Recipe, RecipeIngredient, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.

class RecipeIngredientInLine(admin.TabularInline):
  model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
  inlines = [RecipeIngredientInLine,]

class ProfileInLine(admin.StackedInline):
  model = Profile
  can_delete = False

class UserAdmin(admin.BaseUserAdmin):
  inlines = [ProfileInLine,]

admin.site.register(Recipe, RecipeAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
