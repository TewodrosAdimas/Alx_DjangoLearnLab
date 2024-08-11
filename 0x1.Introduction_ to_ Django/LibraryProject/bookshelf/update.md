<!-- Import the Book model -->
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

<!-- setup object for update using get methode
book_to_update = Book.objects.get(title="1984")

replace old by new and save the change
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save() -->