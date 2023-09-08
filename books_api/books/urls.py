# billing/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BooksListCreateView.as_view(), name='books-list-create'),
]
