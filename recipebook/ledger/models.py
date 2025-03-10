from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Ingredient(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('ledger:ingredient', args=[str(self.name)])

class Recipe(models.Model):
  name = models.CharField(max_length=100)
  author = models.CharField(max_length=50, default='Anonymous')
  CreatedOn = models.DateField(auto_created=True)
  UpdatedOn = models.DateField(auto_now=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('ledger:recipe', args=[str(self.pk)])

class RecipeIngredient(models.Model):
  quantity = models.CharField(max_length=100)
  ingredient = models.ForeignKey(
    Ingredient,
    on_delete=models.CASCADE,
    related_name='recipe'
  )
  recipe = models.ForeignKey(
    Recipe,
    on_delete=models.CASCADE,
    related_name='ingredients'
  )