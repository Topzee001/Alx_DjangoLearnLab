
# Delete Book Instance
command:

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()

output:
(1, {'bookshelf.Book': 1})
<QuerySet []>