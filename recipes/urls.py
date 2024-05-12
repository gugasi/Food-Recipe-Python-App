from django.urls import path
from . import views

'app/model_viewtype'
'recipes/recipe_detail.html'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='homepage'), #this function takes as a parameter.
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/create/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipe-update'), 
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe-delete'), 
    path('about/', views.about, name='aboutpage'),
    path('search/', views.search_recipe, name='search-recipe'),
]
