from django.views.generic import *
from .models import *

class AuthorListView(ListView):
    model = Author

class AuthorCreateView(CreateView):
    model = Author
    fields = ["first_name", "last_name"]
    success_url = "/authors"

class AuthorUpdateView(UpdateView):
    model = Author
    fields = ["first_name", "last_name"]
    success_url = "/authors"

class AuthorDeleteView(DeleteView):
    model = Author
    success_url = "/authors"

class RecipeListView(ListView):
    model = Recipe

class RecipeCreateView(CreateView):
    model = Recipe
    fields = ["title", "author", "ingredients", "instructions"]
    success_url = "/"

class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ["title", "author", "ingredients", "instructions"]
    success_url = "/"

class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = "/"
