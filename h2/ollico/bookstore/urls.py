from django.urls import path
from .views import *

urlpatterns = [
		path('about', AboutView.as_view()),
        path('', HomeView.as_view()),
        path('booklist', BookListView.as_view())
]
