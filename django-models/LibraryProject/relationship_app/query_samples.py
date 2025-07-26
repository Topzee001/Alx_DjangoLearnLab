from .models import Author, Book, Library, Librarian

# query all books by a specific author
author_mame = "author_name"
author = Author.objects.get(name=author_mame)
books = Book.objects.filter(author=author)

# List all authors
allAuthors = Author.objects.all()
# List all books in a library
allBooks = Book.objects.all()
# Retrieve the librarian for a library
library_name = "library_name"
library = Library.objects.get(name=library_name)

librarian = library.librarian
