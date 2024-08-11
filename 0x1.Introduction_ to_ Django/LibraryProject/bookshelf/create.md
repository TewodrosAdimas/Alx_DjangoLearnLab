<!-- Import the Book model -->
from bookshelf.models import Book

<!-- create instance of Book named Book and insert data  -->
book=Book(title = "1984", author = "George Orwell", publication_year = 1949)
book.save