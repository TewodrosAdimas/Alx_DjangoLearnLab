from django.shortcuts import render
from .models import Book

from django.urls import path
from .views import list_books, LibraryDetailView

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
