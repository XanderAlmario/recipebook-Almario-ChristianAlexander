from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    redirect_field_name = 'registration/login.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_add.html'
    redirect_field_name = 'registration/login.html'


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'recipe_image_add.html'
    redirect_field_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        ctx['pk'] = pk
        ctx['recipe'] = Recipe.objects.get(pk=pk)
        ctx['form'] = RecipeImageForm()
        return ctx

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        form = RecipeImageForm(request.POST, request.FILES)

        if form.is_valid():
            r = RecipeImage()
            r.image = request.FILES.get('image')
            r.description = request.POST.get('description')
            r.recipe = Recipe.objects.get(pk=pk)
            r.save()

            return redirect(reverse('ledger:recipe', args=[pk]))
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
    