from django.urls import path
from .views import (BookCreateView,
                    BookListView,
                    BookDetailView,
                    BookUpdateView,
                    BookDeleteView
                    )

urlpatterns = [
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/list/', BookListView.as_view(), name='book-list'),
    path('books/details/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]