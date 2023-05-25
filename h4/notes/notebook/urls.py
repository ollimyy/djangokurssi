from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
        path('', NoteListView.as_view()),
        path('note/new', NoteCreateView.as_view()),
        path('note/<int:pk>', NoteUpdateView.as_view()),
        path('note/<int:pk>/delete', NoteDeleteView.as_view()),
        path('subjects', SubjectListView.as_view()),
        path('subject/new', SubjectCreateView.as_view()),
        path('subject/<int:pk>', SubjectUpdateView.as_view()),
        path('subject/<int:pk>/delete', SubjectDeleteView.as_view()),
        path('accounts/login/', LoginView.as_view()),

]
