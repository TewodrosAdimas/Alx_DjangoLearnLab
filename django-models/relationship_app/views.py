from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()  # Query all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})
