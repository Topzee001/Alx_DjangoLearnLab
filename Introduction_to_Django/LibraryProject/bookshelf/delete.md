
# Delete Book Instance
command:

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
output: 
(1, {'bookshelf.Book': 1})
Book.objects.all()
output:
<QuerySet []>