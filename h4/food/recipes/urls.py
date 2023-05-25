from django.urls import path
from .views import *

urlpatterns = [
        path('', RecipeListView.as_view()),
        path('recipe/new', RecipeCreateView.as_view()),
        path('recipe/<int:pk>', RecipeUpdateView.as_view()),
        path('recipe/<int:pk>/delete', RecipeDeleteView.as_view()),
        path('authors', AuthorListView.as_view()),
        path('author/new', AuthorCreateView.as_view()),
        path('author/<int:pk>', AuthorUpdateView.as_view()),
        path('author/<int:pk>/delete', AuthorDeleteView.as_view()),
]