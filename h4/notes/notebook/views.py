from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

class NoteListView(LoginRequiredMixin, ListView):
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

class SubjectListView(ListView):
    model = Subject

class SubjectCreateView(CreateView):
    model = Subject
    fields = ["name"]
    success_url = "/subjects"

class SubjectUpdateView(UpdateView):
    model = Subject
    fields = ["name"]
    success_url = "/subjects"

class SubjectDeleteView(DeleteView):
    model = Subject
    success_url = "/subjects"


