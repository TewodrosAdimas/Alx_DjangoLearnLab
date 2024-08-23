# from relationship_app.models import Author
from .models import Author, Library, Librarian

book = Author.objects.filter(name = "bealu")
all_books = Library.objects.all()
all_librarian = Librarian.objects.all()
for librarian in all_librarian:
    print (librarian.name)