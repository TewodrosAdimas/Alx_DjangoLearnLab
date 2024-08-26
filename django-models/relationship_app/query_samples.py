# from relationship_app.models import Author
from .models import Author, Library, Librarian, Book


author = "John Doe"
books_by_author = Book.objects.filter(author=author)

library_name = "Central Library"
books_in_library = Library.objects.get(name=library_name).books.all()


library = "Central Library"
librarian = Librarian.objects.get(library=library)


# Author.objects.get(name=author_name)