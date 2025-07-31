
# Delete Book Instance
command:
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()

output:
(1, {'bookshelf.Book': 1})
<QuerySet []>