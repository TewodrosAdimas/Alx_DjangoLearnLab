<!-- import model -->
from bookshelf.models import Book
book = Book.objects.get(title="1984")
    print(book.author) 


<!-- setup a query set
all_books = Book.objects.all()
iterate over object and retrive it's content 
for book in all_books:
    print(book.title)
    print(book.author)
    print(book.publication_year) -->
