from django.shortcuts import render
from .models import Librarian, Library, Book, Author
# Create your views here.

def BookList(request):
    all_books = Book.objects.all()
    return render(request, "list_books.html", all_books)
