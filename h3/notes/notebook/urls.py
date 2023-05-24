from django.urls import path
from .views import *

urlpatterns = [
        path('', NoteListView.as_view()),
        path('note/<int:pk>', NoteUpdateView.as_view()),
        path('note/new', NoteCreateView.as_view()),
        path('note/<int:pk>/delete', NoteDeleteView.as_view()),
]
