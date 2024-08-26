# from relationship_app.models import Author
from .models import Author, Library, Librarian, Book


author = "John Doe"
books_by_author = Book.objects.filter(author__name=author)

library_name = "Central Library"
books_in_library = Library.objects.get(name=library_name).books.all()


librarian_name = "Jane Smith"
library_managed_by_librarian = Library.objects.get(library__name=librarian_name)

# Author.objects.get(name=author_name)