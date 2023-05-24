from django.views.generic import *
from .models import *

class NoteListView(ListView):
    model = Note

class NoteUpdateView(UpdateView):
    model = Note
    fields = ["title", "content", "subject"]
    success_url = "/"

class NoteCreateView(CreateView):
    model = Note
    fields = ["title", "content", "subject"]
    success_url = "/"

class NoteDeleteView(DeleteView):
    model = Note
    success_url = "/"


