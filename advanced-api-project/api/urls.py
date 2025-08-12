from django.urls import path
from .views import (BookCreateView,
                    BookListView,
                    BookDetailView,
                    BookUpdateView,
                    BookDeleteView
                    )

urlpatterns = [
    path('books/create/', BookCreateView.as_view(), name='books'),
    path('books/list/', BookListView.as_view(), name='books'),
    path('books/details/<int:pk>/', BookDetailView.as_view(), name='books'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='books'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='books'),
]