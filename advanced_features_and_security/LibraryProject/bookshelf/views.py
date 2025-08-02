from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.http import HttpResponse
from .forms import ExampleForm, BookForm


# Create your views here.
# any group with this permission can view all books
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    # return render(request, 'books/list.html', {'books': books})
    return HttpResponse("You have permission to view a book.")

# any user with permission can create book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # # logic to add book
    # if request.method == 'POST':
    #     title = request.POST['title']
    #     author = request.POST['author']
    #     publication_year = request.POST['publication_year']
    #     book = Book(title=title, author=author, publication_year=publication_year)
    #     book.save()
    #     return redirect('book_list')
    # return render(request, 'books/add.html')
     return HttpResponse("You have permission to create a book.")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
   # # logic to edit book
    # if request.method == 'POST':
    #     book.title = request.POST['title']
    #     book.author = request.POST['author']
    #     book.publication_year = request.POST['publication_year']
    #     book.save()
    #     return redirect('book_list')
    # return render(request, 'books/edit.html', {'books/edit.html': book})
    return HttpResponse("You have permission to edit a book.")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    # # logic to delete book
    # book = Book.objects.get(pk=pk)
    # book.delete()
    return redirect('book_list')

def search_books(request):
    form = ExampleForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['q']
        books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method =='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form})



