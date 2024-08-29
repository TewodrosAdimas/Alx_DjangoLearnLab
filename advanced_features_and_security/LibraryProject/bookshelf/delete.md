<!-- Import the Book model -->
from bookshelf.models import Book

<!-- select the attribute to be deleted and delete it -->
book = Book.objects.get(title= "Nineteen Eighty-Four")
book.delete()

(1, {'bookshelf.Book': 1})