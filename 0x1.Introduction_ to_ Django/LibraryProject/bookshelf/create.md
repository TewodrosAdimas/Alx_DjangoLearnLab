<!-- Import the Book model -->
from bookshelf.models import Book

<!-- create instance of Book named Book and insert data  -->
book = Book.objects.create(
    title="The Lord of the Rings",
    author="J.R.R. Tolkien",
    publication_year=1954
)

book.save()