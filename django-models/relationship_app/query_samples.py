# from relationship_app.models import Author
from .models import Author, Library, Librarian, Book

author = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(author=author)

all_books = Library.objects.all()
all_librarian = Librarian.objects.all()
for librarian in all_librarian:
    print (librarian.name)

    # relationship_app/query_samples.py
    # doesn't contain: ["Library.objects.get(name=library_name)", "books.all()"]