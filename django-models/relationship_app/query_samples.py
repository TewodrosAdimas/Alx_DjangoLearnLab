# from relationship_app.models import Author
from .models import Author, Library, Librarian, Book


author_name = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(author=author_name)

library_name = Library.objects.get(name="Some Library Name")
books_in_library = library_name.books.all()

all_librarian = Librarian.objects.all()


for librarian in all_librarian:
    print (librarian.name)

#    Author.objects.get(name=author_name)"]