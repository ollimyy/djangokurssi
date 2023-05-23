from django.views.generic import TemplateView, ListView
from .models import *

class AboutView(TemplateView):
    template_name = "bookstore/about.html"

class HomeView(TemplateView):
    template_name = "bookstore/home.html"

class BookListView(ListView):
    model = Book