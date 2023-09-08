from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class BooksListCreateView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

