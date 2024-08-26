from typing import Any
from django.shortcuts import render
from .models import Librarian, Library, Book, Author
from django.views.generic import ListView, DetailView
# Create your views here.

def BookList(request):
    all_books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", all_books)
class ListAllBooks(ListView):
    template_name = 'books/book_list.html'
    context_object_name = 'books'  # Name to use in the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library_name = "Central Library"
        library = Library.objects.get(name=library_name)
        context['books'] = library.books.all()       
        return context
