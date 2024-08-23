# from relationship_app.models import Author
from .models import Author, Library, Librarian, Book

author_name = "author_name"
author = Author.objects.get(name= author_name)
books_by_author = Book.objects.filter(author=author)

all_books = Library.objects.all()
all_librarian = Librarian.objects.all()
for librarian in all_librarian:
    print (librarian.name)

#    Author.objects.get(name=author_name)"]