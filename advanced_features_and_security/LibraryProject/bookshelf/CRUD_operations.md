# Create Book Instance
command

from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

output:

<Book: 1984>

# Retrieve Book Instance

command:
book = Book.objects.get(title="1984")
book.title
book.author
book.publication_year

output:
'1984'
'George Orwell'
1949

# Update Book Title

command:
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title

output:
'Nineteen Eighty-Four'

# Delete Book Instance

command:

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
output: 
(1, {'bookshelf.Book': 1})
Book.objects.all()

output:
<QuerySet []>