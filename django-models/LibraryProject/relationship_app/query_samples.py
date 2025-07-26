from .models import Author, Book, Library, Librarian

# query all books by a specific author
author_mame = "author_name"
author = Author.objects.get(name=author_mame)
books = Book.objects.filter(author=author)

# list all books in a library
library_name = "library_name"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
# Retrieve the librarian for a library

librarian = library.librarian
