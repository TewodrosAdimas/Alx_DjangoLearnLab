<!-- create -->
from bookshelf.models import Book
book=Book(title = "1984", author = "George Orwell", publication_year = 1949)
book.save()

<!-- retrive -->
from bookshelf.models import Book
all_books = Book.objects.all()
for book in all_books:
    print(book.title)
    print(book.author)
    print(book.publication_year)

<!-- 
    output:
    1984
    George Orwell
    1949 -->

<!-- Update -->
from bookshelf.models import Book
book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()

<!-- Delete -->
from bookshelf.models import Book
book = Book.objects.get(title= "Nineteen Eighty-Four")
book.delete()

<!-- output
(1, {'bookshelf.Book': 1}) -->