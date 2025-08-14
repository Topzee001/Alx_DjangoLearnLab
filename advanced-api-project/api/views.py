from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import (Book)
from .serializers import (BookSerializer)
from django_filters import rest_framework
# import DjangoFilterBackend
# import django_filters


# Create your views here.

class BookListView(generics.ListAPIView):
    """List all books with optional filter by author or title."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'publication_year', 'title']  # Allow filtering by author or title, e.g., /books/?author=John%20Doe
    search_fields = ['author__name', 'title']
    ordering_fields = ['title', 'author']

    # TODO: sort the icontains filter for search

    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveAPIView):
    """retrieve a single book by ID"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """create a new book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """save the book with current user with created_by """
        serializer.save(created_by=self.request.user)

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        """save the book with the current user as updated_by."""
        serializer.save(created_by=self.request.user)


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticated]

