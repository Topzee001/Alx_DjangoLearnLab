from .models import Author, Book, Library, Librarian

# query all books by a specific author
author = Author.objects.get(name="Author Name")
books = author.books.all()
# List all books in a library
allBooks = Book.objects.all()
# Retrieve the librarian for a library
library_name = "Library Name"
library = Library.objects.get(name=library_name)

librarian = library.librarian
