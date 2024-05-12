from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import recipe

from . import models

# Create your views here.
def homepage(request):
    recipes = models.recipe.objects.all() #This will override to what I am trying to pass here.
    context = {
        'recipes': recipes #This is the recipes data from above that I want to display on the homepage
    }
    return render(request, 'recipes/home.html ', context) #This is the homepage.html file that I want to display on the homepage with the context data')

class RecipeListView(ListView):
    model = models.recipe
    template_name = 'recipes/home.html' # <app>/<model>_<viewtype>.html BY DEFAULT it is called the object.
    context_object_name = 'recipes' #This is the recipes data from above that I want to display on the homepage that I override

class RecipeDetailView(DetailView):
    model = models.recipe

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.recipe
    fields = ['name', 'ingredients', 'instructions', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.recipe
    fields = ['name', 'ingredients', 'instructions', 'image']

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.recipe
    success_url = reverse_lazy('homepage')

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False

def about(request):
    return render(request, 'recipes/about.html', {'title': 'About'})

def search_recipe(request):
    query = request.GET.get('q')
    results = recipe.objects.filter(name__iexact=query)
    context = {'results': results, 'query': query}
    return render(request, 'recipes/search_results.html', context)
